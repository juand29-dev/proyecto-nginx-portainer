from flask import Flask

sample = Flask(__name__)

MYSQL_PASSWORD = "super_secret_123"

@sample.route("/")
def home():
    return {"message": "Aplicación de prueba"}, 200

if __name__ == "__main__":
    sample.run(debug=True)
