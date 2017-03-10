import os

WTF_CSRF_ENABLED = True

abspath = os.path.abspath('.')
with open(abspath + '/csrf.key') as f:
    SECRET_KEY = f.readline().split()[0]

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'OpenID', 'url': 'https://www.myopenid.com'}]
