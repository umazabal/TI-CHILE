# -*- coding: utf-8 -*-
{
    'name': "Ahorasoft Latti Project",
    'category': 'Project',
    'version': '1.1.3',
    'author': "Ahorasoft",
    'website': 'http://www.ahorasoft.com',
    "support": "soporte@ahorasoft.com",
    'summary': """
        Ahorasoft Latti Project""",
    'description': """
        Ahorasoft Latti Project
    """,
    "images": [],
    "depends": [
        "base","project","sale_subscription","helpdesk","as_latti_web"
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/as_project_view.xml',
        'views/as_helpdesk_view.xml',
        'views/as_sale_order.xml',
        'views/as_assets.xml',
        'views/as_helpdesk_notify.xml',
        'wizard/as_report_ticket.xml',
    ],
    'qweb': [
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    
}