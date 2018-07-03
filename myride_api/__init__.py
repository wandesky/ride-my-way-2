from flask import Flask 

app = Flask(__name__)

from myride_api.api.routes import mod
from myride_api.site.routes import mod


app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
