import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello', methods=['POST'])
def hello():
    data = json.loads(flask.request.data)
    name = data.get('name', 'World')
    return f'Hello, {name}!'

@app.route('/<string:name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)