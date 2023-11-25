import scrypto
from cipher.scrypto import generate_key, bytes_to_string
from djangochat import settings

if __name__ == "__main__":
    # key = generate_key()
    # e = scrypto.encrypt('sssssssssssss siu đệp trẠi.', key)
    f = b'\x19\x07\x0e\x03I'
    print(bytes_to_string(f))
    print((bytes_to_string(f)))
    d = scrypto.decrypt(bytes("b'\x19\x07\x0e\x03I'", 'utf-8'), settings.DJANGO_CHAT_SECRET_KEY)
    # print(key)
    # print(e)
    print(d)