import json
from flask import jsonify
from src.helper.sendmessagetophone import sendMessageToPhone
from src.helper.aes import AESCipher


def genEncryptedData(data):
    sha255_key = data['sha255_key']
    details = {
        "name": data['name'],
        "aadharaNumber": data['aadharaNumber'],
        "address": data['address'],
        "phoneNumber": data['phoneNumber'],
    }
    result = AESCipher(sha255_key).encrypt(json.dumps(details))
    sendMessageToPhone(result)
    return jsonify({"encryptData": result})
