activate_this = '/var/www/html/sstech/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys

sys.path.insert(0, "/var/www/html/sstech")

from app import app

application = app
