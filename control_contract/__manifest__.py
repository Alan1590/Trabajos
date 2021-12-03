# -*- coding: utf-8 -*-
{
    'name': "Extend acoount move line",

    'description': """

    """,

    'author': "Alan Gon",
    'website': "",

    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contract'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
        'views/account_move_view_extend.xml',
        'report/account_move_report_extend.xml',
    ],
}
