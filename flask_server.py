from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Vlas"


@app.route("/user")
def getuser():
    user={
        "name": "Vlas",
        "age" : 4
    }
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug = True)