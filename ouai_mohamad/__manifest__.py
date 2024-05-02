{
    
    
    'name' : 'ouai_mohamad',
    'shortdesc' : 'ouai ouia ouai',
    'summary': "mohamad",

    'description': "description",

    'author': "Mohamad",
    'website': "http://www.melissa.com",
    'category': 'Tool',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', ],
    'installable' : True,
    'auto_install': False,
    'application' : True,
    # always loaded
    'data': [
    'views/res_partner_views.xml',
    'security/ir.model.access.csv',

    ],
    # 'images': ['static/src/img/icon.png'],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}