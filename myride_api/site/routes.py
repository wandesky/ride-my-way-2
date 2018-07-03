from flask import Blueprint

mod = Blueprint('site', __name__)

@mod.route('/')
def homepage():
	return '<h1>Hmmm! You must be a new one here</h1><p>Try configuring your path to something like --hostname--/api/v1/ and see you on the other side</p>'