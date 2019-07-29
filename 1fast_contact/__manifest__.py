# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': '1Fast Contacts',
    'category': 'Tools',
    'summary': 'Custom contact for 1Fast',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts. and add more field contact for 1Fast.
""",
    'depends': ['base', 'mail'],
    'data': [
        'views/1fast_contact_views.xml',
    ],
    'application': True,
}
