"""Summary
"""
# © 2016 ADHOC SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields, _
from odoo.exceptions import ValidationError, Warning
import datetime
from dateutil.relativedelta import relativedelta

import ast
import logging

_logger = logging.getLogger(__name__)

class control_contract(models.Model):
    _name = "contract.contract"
    _inherit = "contract.contract"

    external_id = fields.Integer("External ID")
    state_control = fields.Selection ([
        ('normal','Normal'),
        ('failed_invoice','Sin factura'),
        ],default='normal')

    def exist_invoice(self,date_invoice,name_contract):
        exist = self.env['account.move'].search_count([('&'),
            ('date_invoice','<=',date_invoice),('invoice_origin','=',name_contract)])
        return exist

    def control_invoices(self):
        all_contract = self.search([])
        for contract in all_contract:
            invoice_date = contract.recurring_next_date  - relativedelta(months=1)
            if self.exist_invoice(invoice_date,contract.name) == 0:
                contract.state_control = 'failed_invoice'
            else:
                contract.state_control = 'normal'

    @api.model
    def recurring_create_invoice(self):
        invoice = super(control_contract, self).recurring_create_invoice()
        self.state_control = 'normal'
        return invoice





