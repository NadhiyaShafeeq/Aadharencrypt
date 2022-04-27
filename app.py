import json
from flask import Flask, request
from src.service.decryptData import genDecryptedData
from src.service.encryptData import genEncryptedData
from src.service.genarateToken import genToken
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Online voting system using blockchain</h1>"


@app.route("/api/v1/genarate-token", methods=['POST'])
def genarateToken():
    data = request.get_json()
    return genToken(data)


@app.route("/api/v1/encrpt-data", methods=['POST'])
def encryptData():
    data = request.get_json()
    return genEncryptedData(data)


@app.route("/api/v1/decrpt-data", methods=['POST'])
def dencryptData():
    data = request.get_json()
    return genDecryptedData(data)


if __name__ == "__main__":
    app.run(debug=True)
