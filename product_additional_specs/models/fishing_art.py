# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class FishingArt(models.Model):
    _name = "fishing.art"

    name = fields.Char(
        string="Fishing art",
        required=True,
        index=True,
        tracking=True,
    )
