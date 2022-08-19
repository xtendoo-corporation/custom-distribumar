# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ConservationMethod(models.Model):
    _name = "conservation.method"

    name = fields.Char(
        string="Conservation method",
        required=True,
        index=True,
        tracking=True,
    )
