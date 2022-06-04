{
    'name': 'A3 Quality Assurance',
    'version': '1.0',
    'summary': 'Supports auality assurance processes, including course portfolio management, as well as ILO and SO assessment.',
    'category': 'Liberal Arts Education',
    'author': 'Omar IRAQI',
    'maintainer': 'Omar IRAQI',
    'website': '',
    'license': 'LGPL-3',
    'contributors': [
        '',
    ],
    'depends': [
        'a3catalog',
        'a3roster',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/course_program_view.xml',
        "views/accreditation_view.xml",
        "views/portfolio_view.xml",
        "views/program_view.xml",
        "views/a3quality_menu.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
