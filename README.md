# Odoo Local Development Environment

A Docker-based local development environment for Odoo 17.0 with Nginx reverse proxy, PostgreSQL database, and pgAdmin for database management.

## Features

- 🐳 **Docker Compose** setup for easy deployment
- 🔧 **Odoo 17.0** with development mode enabled
- 🗄️ **PostgreSQL 17** database
- 🌐 **Nginx** reverse proxy with SSL/HTTPS support
- 📊 **pgAdmin** for database administration
- 📁 **Volume mounts** for persistent data and custom addons
- 🔒 **SSL certificates** support for secure connections

## Services

| Service | Description | Access |
|---------|-------------|--------|
| **Odoo** | Main Odoo application server | `https://{ODOO_HOSTNAME}` |
| **PostgreSQL** | Database server | Internal network only |
| **Nginx** | Reverse proxy with SSL termination | Ports 80/443 |
| **pgAdmin** | Database administration tool | `https://{PGADMIN_HOSTNAME}` |

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- [mkcert](https://github.com/FiloSottile/mkcert) for generating local SSL certificates (see SSL Setup section)

### Setup

1. **Clone and navigate to the project:**

   ```bash
   git clone https://github.com/yourusername/odoo-local-dev.git
   cd odoo-local-dev
   ```

2. **Create environment file:**

   ```bash
   cp .example.env .env
   ```

3. **Configure your environment:**

   Edit `.env` file with your specific settings:

   ```env
   # Odoo Configuration
   ODOO_TAG=17
   ODOO_HOSTNAME=your-odoo.local
   ODOO_PORT=8069
   
   # Database Configuration
   HOST=postgres
   USER=odoo
   PASSWORD=your_secure_password
   
   # Nginx Configuration
   NGINX_TAG=1.27.4
   NGINX_HOSTNAME=nginx.local
   
   # PostgreSQL Configuration
   POSTGRES_TAG=17
   POSTGRES_DB=odoo
   POSTGRES_USER=odoo
   POSTGRES_PASSWORD=your_secure_password
   
   # pgAdmin Configuration
   PGADMIN_HOSTNAME=pgadmin.local
   PGADMIN_TAG=9.6.0
   PGADMIN_DEFAULT_EMAIL=admin@example.com
   PGADMIN_DEFAULT_PASSWORD=secure_admin_password
   PGADMIN_PORT=80
   ```

4. **Add hostnames to your hosts file:**

   ```bash
   # Windows: C:\Windows\System32\drivers\etc\hosts
   # Linux/Mac: /etc/hosts
   127.0.0.1 your-odoo.local
   127.0.0.1 pgadmin.local
   127.0.0.1 nginx.local
   ```

5. **Start the services:**

   ```bash
   docker-compose up -d
   ```

## SSL Certificate Setup

The Nginx configuration expects SSL certificates in the `nginx/certs/` directory. You have several options:

### mkcert (Recommended for Development)

```bash
# Install mkcert (if not already installed)
# Windows: choco install mkcert
# Mac: brew install mkcert
# Linux: Check your package manager

# Create local CA
mkcert -install

# Generate certificates
cd nginx/certs
mkcert your-odoo.local pgadmin.local nginx.local
```

## Directory Structure

```text
odoo-local-dev/
├── docker-compose.yml      # Main Docker Compose configuration
├── .env                   # Environment variables (create from .example.env)
├── .example.env           # Environment template
├── README.md              # This file
├── addons/                # Custom Odoo addons directory
├── config/
│   └── odoo.conf          # Odoo configuration file
├── data/
│   ├── filestore/         # Odoo file storage
│   ├── modules/           # Odoo core modules (volume mount)
│   └── sessions/          # Odoo session data
├── nginx/
│   ├── certs/             # SSL certificates
│   └── templates/         # Nginx configuration templates
└── postgres-data/
    └── data/              # PostgreSQL data directory
```

## Usage

### Starting Services

```bash
# Start all services
docker-compose up -d

# Start specific service
docker-compose up -d odoo

# View logs
docker-compose logs -f odoo
```

### Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (⚠️ This will delete data)
docker-compose down -v
```

### Accessing Services

- **Odoo**: `https://your-odoo.local`
- **pgAdmin**: `https://pgadmin.local`
- **Nginx**: `https://nginx.local`

### Managing Custom Addons

1. Place your custom addons in the `addons/` directory
2. Restart Odoo service: `docker-compose restart odoo`
3. Update apps list in Odoo interface
4. Install your custom modules

### Database Management

**Using pgAdmin:**

1. Access pgAdmin at `https://pgadmin.local`
2. Login with credentials from `.env` file
3. Add server with connection details:
   - Host: `postgres`
   - Port: `5432`
   - Database: `odoo`
   - Username/Password: From `.env` file

**Using psql:**

```bash
docker-compose exec postgres psql -U odoo -d odoo
```

## Accessing Odoo Shell

You can access the Odoo shell for advanced operations:

```bash
docker-compose exec -it odoo sh

# Then run the Odoo shell command

# Example command to scaffold a new module:

$ odoo scaffold estate /mnt/extra-addons

# Exit:
$ exit
```

## Configuration

### Odoo Configuration

The main Odoo configuration is in `config/odoo.conf`. Key settings include:

- Development mode enabled
- Debug logging
- Database filtering by hostname
- Proxy mode enabled for Nginx

### Nginx Configuration

Nginx is configured to:

- Redirect HTTP to HTTPS
- Terminate SSL connections
- Proxy requests to appropriate services
- Support multiple hostnames

## Troubleshooting

### Common Issues

1. **SSL Certificate Errors:**
   - Ensure certificates exist in `nginx/certs/`
   - Check certificate names match hostnames
   - For self-signed certificates, accept browser warnings

2. **Database Connection Issues:**
   - Verify PostgreSQL service is running: `docker-compose ps`
   - Check database credentials in `.env` file
   - Ensure database is created: `docker-compose logs postgres`

3. **Odoo Not Accessible:**
   - Check Odoo logs: `docker-compose logs odoo`
   - Verify hostname in `.env` matches hosts file entry
   - Ensure port 8069 is not blocked

4. **Permission Issues:**
   - Check volume mount permissions
   - Ensure Docker has access to project directory

### Useful Commands

```bash
# View service status
docker-compose ps

# Follow logs for all services
docker-compose logs -f

# Access Odoo container shell
docker-compose exec odoo bash

# Backup database
docker-compose exec postgres pg_dump -U odoo odoo > backup.sql

# Restore database
docker-compose exec -T postgres psql -U odoo odoo < backup.sql
```

## Development Tips

1. **Enable Developer Mode:** Access Odoo settings and enable developer mode for additional development tools
2. **Custom Addons:** Place custom modules in `addons/` directory for automatic loading
3. **Database Reset:** Remove `postgres-data/data/` directory to start with fresh database
4. **Live Reload:** Odoo runs with `--dev all` flag for automatic code reloading

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:

1. Check the troubleshooting section
2. Review Docker Compose and service logs
3. Consult Odoo documentation for application-specific issues

 docker exec -it odoo-dev sh
$ odoo shell scafold
Usage: odoo shell [options]