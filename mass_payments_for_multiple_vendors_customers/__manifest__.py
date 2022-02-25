# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Mass Register Payment for Multiple Vendor Bills & Customer Invoices (Credit Notes, Refunds, Receipts)',
    'version' : '1.0',
    'summary' : """
        Mass Register Payment for Multiple Vendor Bills & Customer Invoices (Credit Notes, Refunds, Receipts),
        Multiple Vendor Payment,
        Multiple Bill Payment,
        Multiple Customer Payment,
        Multiple Invoice Payment,
        Invoice Bulk Payment,
        Customer Bulk Payment,
        Vendor Bulk Payment,
        Bill Bulk Payment,
        Mass Invoice Payment,
        Mass Payment,
        mass bill payment,
        mass vendor payment,
        Mass payment invoice,
        Mass Payments,
        Customer Invoices mass payment,
        Vendor Bills mass payment,
        Credit Notes (Customer Credit Note),
        Sales Receipt mass payment,
        Refunds (Vendor Credit Note) mass payment,
        Purchase Receipt  mass payment,
        multiple payments,
        Odoo standard App,
    """,
    'category': 'Accounting',
    'sequence': 1,
    'author' : 'OMAX Informatics',
    'website': 'www.omaxinformatics.com',
    'description' : """
    """,
    'depends' : ['base','account'],
    'data' : [
      'security/ir.model.access.csv',
      'wizard/multiple_register_payments.xml',
     ],
    'license': 'AGPL-3',
    'currency': 'EUR',
    'price': 15.00,
    'images': ['static/description/banner.jpg',],
    'demo' : [],
    'test': [],
    'application': True,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
