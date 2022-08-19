# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductionMethod(models.Model):
    _name = "production.method"

    name = fields.Char(
        string="Production method",
        required=True,
        index=True,
        tracking=True,
    )
