# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class Agreement(models.Model):
    _inherit = "agreement"

    contract_type = fields.Selection(
        selection=[("sale", "Customer"), ("purchase", "Supplier")],
    )
    contract_id = fields.Many2one("contract.contract")
