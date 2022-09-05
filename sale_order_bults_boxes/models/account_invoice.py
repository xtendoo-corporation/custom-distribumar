# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    bults = fields.Float(
        string="Bults",
        store=True,
    )
    boxes = fields.Float(
        string="Boxes",
        store = True,
    )
