from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return jsonify(message="Welcome to Code Kamikaze, And Subscribe to Code Kamikaze")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
