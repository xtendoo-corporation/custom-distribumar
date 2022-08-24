# Copyright 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2017-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    pending = fields.Float(
        string="Pending", digits="pending", group_operator="avg"
    )

    def _select(self):
        res = super()._select()
        res = res.replace("l.product_id,", self._get_discounted_pending())
        return res

    def _group_by(self):
        res = super()._group_by()
        res += ", pending"
        return res

    def _get_discounted_pending(self):
        """Inheritable method for getting the SQL expression used for
        calculating the unit price with discount(s).

        :rtype: str
        :return: SQL expression for discounted unit price.
        """
        return "l.product_id, (CASE WHEN po.force_received THEN 0 ELSE l.qty_pending_received END) as pending,"

