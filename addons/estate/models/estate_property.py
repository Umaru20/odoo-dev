from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    # Availability date should not be copied when duplicating a record
    date_availability = fields.Date(string="Available From", copy=False)
    expected_price = fields.Float(string="Expected Price", required=True)
    
    # Selling price should not be editable by users
    # and should not be copied when duplicating a record
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Has Garage?")
    garden = fields.Boolean(string="Has Garden?")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation"
    )

'''from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Property Name", required=True)
    description = fields.Text(string="Property Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date of Availability")
    expected_price = fields.Float(string="Expected Selling Price", required=True)
    selling_price = fields.Float(string="Final Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Number of Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Includes Garage?")
    garden = fields.Boolean(string="Includes Garden?")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        [
            ('north', 'Facing North'),
            ('south', 'Facing South'),
            ('east', 'Facing East'),
            ('west', 'Facing West')
        ],
        string="Garden Orientation"
    )'''
