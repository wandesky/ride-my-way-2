from flask import Flask, jsonify, request

app = Flask(__name__)

rides = [{'driverID' : '001', 'car-route':'routeA','rideID':'ride001'}, {'driverID' : '002', 'car-route':'routeB','rideID':'ride002'}, {'driverID' : '001', 'car-route':'routeA' ,'rideID':'ride003'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify(

            {'version': "You are now running version 1 of the api"},
            {'You should not be here': "Ideally, you are supposed to access the root page using <host>/api/v1/users/"},
            {'So why are you seeing this': "This page was made just to let you know the way things are organised around here"}
            
        )


@app.route('/api/v1/users/', methods=['GET'])
def test():
    return jsonify(
        {'version': "You are now running version 1 of the api"},
        {'instruction': "How to use the api"}
        )

@app.route('/api/v1/users/rides', methods= ['GET'])
def returnAll():
    return jsonify({'rides': rides})

@app.route('/api/v1/users/rides/<string:rideID>', methods=['GET'])
def returnOne(rideID):
    results = [ride for ride in rides if ride['rideID'] == rideID]
    return jsonify({'ride':results[0]})

if __name__ == '__main__':
    app.run()