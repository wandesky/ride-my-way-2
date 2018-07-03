from flask import Blueprint
from . import v1
from . import v2
# from v1 import toto #v1_fetch_rides
# from v2 import v2_fetch_rides

mod = Blueprint('api', __name__)

@mod.route('/v1')
def the_newbie():
	return v1.v1_newbie()

@mod.route('/v1/rides')
def v1_fetch_all_rides():
	return v1.v1_fetch_all_rides()

@mod.route('/v1/rides/<rideId>')
def v1_fetch_specific_rides():
	return v1.v1_fetch_specific_rides()






########### Here comes Version 2 ####################
@mod.route('/v2')
def v2_fetch_all_rides():
	return v2.v2_fetch_all_rides()
