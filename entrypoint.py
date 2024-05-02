from flask import Flask, jsonify, request
from hashlib import sha256
from flask_basicauth import BasicAuth

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

basic_auth = BasicAuth(app)

@app.route('/api/v1/users', methods=['GET'])
@basic_auth.required
def get_users():
    response = {"users": "pipipi"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


