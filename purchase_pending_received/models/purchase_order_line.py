# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    qty_pending_received = fields.Float(
        string="Pending",
        compute="_computed_qyt_pending_received",
        store=True,
    )

    @api.depends('product_qty', 'qty_received')
    def _computed_qyt_pending_received(self):
        for record in self:
            record.qty_pending_received = record.product_qty - record.qty_received

