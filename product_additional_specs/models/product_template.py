# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    scientific_name = fields.Char(
        string="Scientific Name",
        required=True,
        index=True,
        tracking=True,
    )
