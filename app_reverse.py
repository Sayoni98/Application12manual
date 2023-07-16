from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        "d": "1",
        "message": "Hello World"
    }
    return jsonify(data)

@app.route('/reverse')
def reverse():
    response = app.test_client().get('/')
    data = response.get_json()
    data["message"] = data["message"][::-1]
    return jsonify(data)

if __name__ == '__main__':
    app.run()