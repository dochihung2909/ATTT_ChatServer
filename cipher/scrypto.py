import random
from cipher import vncode as vnc


def generate_key():
    values = []
    for _ in range(256):
        values.append(random.randint(0, 255))
    random.shuffle(values)
    return bytes(values)


def encrypt(message, key):
    if type(key) == str:
        key = bytes(key, 'utf-8')
    message_bytes = vnc.encode(message)
    encrypted_message = bytes([a ^ b for a, b in zip(message_bytes, key)])
    return encrypted_message


def decrypt(message, key):
    if type(key) == str:
        key = bytes(key, "utf-8")
    decrypted_message = bytes([a ^ b for a, b in zip(message, key)])
    return vnc.decode(decrypted_message)


def bytes_to_string(bytes) -> str:
    string = str(bytes)

    return string.lstrip('b').lstrip("'").rstrip("'")