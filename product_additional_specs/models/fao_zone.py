# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class FaoZone(models.Model):
    _name = "fao.zone"

    name = fields.Char(
        string="Fao zone",
        required=True,
        index=True,
        tracking=True,
    )
