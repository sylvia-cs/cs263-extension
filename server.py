from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
# Apply CORS to all routes and allow all origins (for development only)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/data', methods=['POST', 'OPTIONS'])  # Ensure OPTIONS is allowed
def receive_data():
    if request.method == 'OPTIONS':
        # This will handle preflight requests
        response = app.make_default_options_response()
    else:
        # Your POST handling code
        data = request.json
        print(data)  # Process the data as needed
        response = app.response_class(
            response=json.dumps({'status': 'Data received'}),
            status=200,
            mimetype='application/json'
        )
    # Set CORS headers for the main request
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
