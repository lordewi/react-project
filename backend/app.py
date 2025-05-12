import time
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
# Allow requests from http://localhost:3000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/exemple', methods=['POST', 'OPTIONS'])
def exemple():
    # time.sleep(2)
    # Handle OPTIONS request (preflight) without token validation
    if request.method == 'OPTIONS':
        return {}, 200  # Return empty response for preflight

    # Handle GET request with token validation
    token = request.headers.get('X-API-Token')
    if token != "votre-token-secret":
        return {"error": "Invalid token"}, 401
    data = request.get_json() or {}
    input_value = data.get('input', '')
    return {"message": input_value}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
