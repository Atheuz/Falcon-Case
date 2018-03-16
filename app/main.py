from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

@app.errorhandler(404)
def bad_input(error=None):
    message = {
            'status': 400,
            'message': 'Bad Request, input was malformed.',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

@app.route('/add', methods=["GET", "POST"])
def index():
    """Help on route '/':

    Sends a GET or POST for adding JSON value to the database.
    
    :param js: String containing the JSON string for GET.
    :param json: JSON containing value for POST."""

    data = None
    if(request.method == "GET"):
        data = request.args.get("js")
        if(data):
            # Check if valid JSON
            try:
                data = json.loads(data)
                data = json.dumps(data)
            except json.decoder.JSONDecodeError as e:
                data = None

    elif (request.method == "POST"):
        data = request.get_json()
        if (data):
            data = json.dumps(data)
        
    if not data:
        return bad_input()
    else:
        resp = jsonify(status=200, message=data)
        resp.status_code = 200
        
        return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)