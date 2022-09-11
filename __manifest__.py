# -*- encoding: utf-8 -*-

{
    "name": "Binary City Client",
    "summary": """
        Binary City Client. 
    """,
    "author": "Peter Mudoko.",
    "website": "https://www.absolutecorporatesolutions.com/",
    "version": "14.0.0.0.0",
    "depends": ['base', 'mail'],
    "data": [

        "security/ir.model.access.csv",
        "data/binary_city_client_seq.xml",

        # "data/mail_template.xml",
        "views/binary_city_client.xml",

        
    ],
    'qweb': [     

    ],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
