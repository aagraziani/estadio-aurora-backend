from flask import jsonify

def index():
    return jsonify({
        'message': 'Hello, World from the Backend!'
        }), 200