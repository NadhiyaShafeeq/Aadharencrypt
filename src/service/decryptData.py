import json
from flask import jsonify
from src.helper.aes import AESCipher


def genDecryptedData(data):
    sha255_key = data['sha255_key']
    encryptData = data['encryptData']
    result = AESCipher(sha255_key).decrypt(encryptData)
    result = json.loads(result)
    return jsonify({"data": result})
