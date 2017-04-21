
#sqlalchemy配置
SQLALCHEMY_DATABASE_URI="mysql://admin:123456@123.56.131.22:3306/springbootwebapp"

#跨域配置
CSRF_ENABLED=True
SECRET_KEY='you-will-never-guess'

#openId配置
OPENID_PROVIDERS =[
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]