from flask import jsonify
from src.helper.hash import hashDataSha256


def genToken(data):
    data = {
        "email": data['email'],
        "name": data['name'],
    }
    hasheddata = hashDataSha256(data)
    return jsonify({"sha255_key": hasheddata})
