
from pgo.member.routes import rmember
from pgo.admin.routes import radmin
from flask import Flask


app = Flask('__name__', template_folder='pgo/templates',
            static_folder='pgo/static')
app.config['SECRET_KEY'] = 'super-secret-random-key'

app.register_blueprint(rmember)
app.register_blueprint(radmin)
