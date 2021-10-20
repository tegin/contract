# Copyright 2021 Ecosoft Co., Ltd (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ContractContract(models.Model):
    _inherit = "contract.contract"

    agreement_ids = fields.One2many(
        comodel_name="agreement",
        inverse_name="contract_id",
        string="Agreement",
        ondelete="restrict",
    )
