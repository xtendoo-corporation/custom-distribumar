# Copyright 2022 Darío Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    scientific_name = fields.Char(
        string="Scientific Name",
        required=False,
        index=True,
        tracking=True,
    )
    tare = fields.Char(
        string="Tare",
        required=False,
        index=True,
        tracking=True,
    )
    scandall = fields.Char(
        string="Scandall",
        required=False,
        index=True,
        tracking=True,
    )
    lot_name = fields.Char(
        string="Lot name",
        required=False,
        index=True,
        tracking=True,
    )
    production_method_id = fields.Many2one(
        comodel_name="production.method",
        string="Production method",
        ondelete="restrict",
    )
    conservation_method_id = fields.Many2one(
        comodel_name="conservation.method",
        string="Conservation method",
        ondelete="restrict",
    )
    fishing_art_id = fields.Many2one(
        comodel_name="fishing.art",
        string="Fishing art",
        ondelete="restrict",
    )
    fao_zone_id = fields.Many2one(
        comodel_name="fao.zone",
        string="Fao zone",
        ondelete="restrict",
    )
