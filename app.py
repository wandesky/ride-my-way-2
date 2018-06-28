from flask import Flask, jsonify, request

app = Flask(__name__)

rides = [{'driverID' : '001', 'car-route':'routeA','rideID':'ride001'}, {'driverID' : '002', 'car-route':'routeB','rideID':'ride002'}, {'driverID' : '001', 'car-route':'routeA' ,'rideID':'ride003'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': "I should be displaying the homepage here"})

@app.route('/rides', methods= ['GET'])
def returnAll():
    return jsonify({'rides': rides})

@app.route('git sta', methods=['GET'])
def returnOne(rideID):
    results = [ride for ride in rides if ride['rideID'] == rideID]
    return jsonify({'ride':results[0]})

if __name__ == '__main__':
    app.run()