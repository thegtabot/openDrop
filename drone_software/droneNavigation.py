# On Raspberry Pi (10.0.0.2)
from flask import Flask, jsonify
from dronekit import connect
import time

app = Flask(__name__)

# Connect to the Pixhawk (adjust connection string as needed)
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)
@app.route('/drone-location')
def drone-location():
    try:
        location = vehicle.location.global_frame
        if location and location.lat is not None and location.lon is not None:
            print('Drone Latititude: 'str(location.lat), ' Longitude: ', str(location.lon) )
            return jsonify({
                'status': 'success',
                'latitude': location.lat,
                'longitude': location.lon,
                'altitude': location.alt
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'GPS location not available.'
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Exception occurred: {str(e)}'
        }), 500

# Ensure the vehicle connection is closed when the Flask app stops
@app.teardown_appcontext
def close_vehicle(exception=None):
    vehicle.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Make accessible over VPN
