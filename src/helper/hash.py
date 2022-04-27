import hashlib


def hashDataSha256(data):
    """
    Hash data with SHA256.
    """
    data = str(data)
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()
