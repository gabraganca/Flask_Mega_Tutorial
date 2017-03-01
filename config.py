import os

WTF_CSRF_ENABLED = True

abspath = os.path.abspath('.')
with open(abspath + '/csrf.key') as f:
    SECRET_KEY = f.readline().split()[0]
