# Copyright 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2017-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    bults = fields.Float(
        string="Bults", digits="bults", group_operator="avg"
    )
    boxes = fields.Float(
        string="Boxes", digits="boxes", group_operator="avg"
    )

    def _select(self):
        res = super()._select()
        res = res.replace("p.product_tmpl_id,", self._get_bults_boxes())
        return res

    def _group_by(self):
        res = super()._group_by()
        res += ", bults"
        res += ", boxes"
        return res

    def _get_bults_boxes(self):
        """Inheritable method for getting the SQL expression used for
        calculating the unit price with discount(s).

        :rtype: str
        :return: SQL expression for discounted unit price.
        """
        return "p.product_tmpl_id, l.bults AS bults, l.boxes AS boxes,"

