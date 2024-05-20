{
    
    
    'name' : 'mohamad_spec',
    'shortdesc' : 'Des modification pour des differents modules pour exercer',
    'summary': "mohamad",

    'description': "description",

    'author': "Mohamad",
    'website': "https://www.linkedin.com/in/mohamad-kattan/",
    'category': 'Tool',
    'version': '0.1',
    'depends': ['base', 'sms'],
    'installable' : True,
    'auto_install': False,
    'application' : True,
    'data': [
    'views/res_partner_views.xml',
    'security/ir.model.access.csv',

    ],
}