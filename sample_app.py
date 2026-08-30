from flask import Flask
import os

sample = Flask(__name__)


@sample.route("/")
def home():
    return {"message": "Aplicación de prueba"}, 200


if __name__ == "__main__":
    sample.run(debug=False)
