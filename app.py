from flask import Flask
from routes.ml_route import ml_route

app = Flask(__name__)


app.register_blueprint(ml_route)

if __name__ == "__main__":
    app.run(debug=True)