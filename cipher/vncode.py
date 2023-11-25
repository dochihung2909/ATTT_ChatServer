# Create the Telex alphabet.
alphabet = {
    "á": "a.s",
    "à": "a.f",
    "ạ": "a.j",
    "ả": "a.r",
    "ã": "a.x",
    "ă": "a.w",
    "ắ": "aws",
    "ằ": "awf",
    "ặ": "awj",
    "ẳ": "awr",
    "ẵ": "awx",
    "â": "a.a",
    "ấ": "aas",
    "ầ": "aaf",
    "ậ": "aaj",
    "ẩ": "aar",
    "ẫ": "aax",
    "é": "e.s",
    "è": "e.f",
    "ẹ": "e.j",
    "ẻ": "e.r",
    "ẽ": "e.x",
    "ê": "e.e",
    "ế": "ees",
    "ề": "eef",
    "ệ": "eej",
    "ể": "eer",
    "ễ": "eex",
    "đ": "d.d",
    "í": "i.s",
    "ì": "i.f",
    "ỉ": "i.r",
    "ị": "i.j",
    "ĩ": "i.x",
    "ó": "o.s",
    "ò": "o.f",
    "ọ": "o.j",
    "ỏ": "o.r",
    "õ": "o.x",
    "ô": "o.o",
    "ố": "oos",
    "ồ": "oof",
    "ộ": "ooj",
    "ổ": "oor",
    "ỗ": "oox",
    "ơ": "o.w",
    "ớ": "ows",
    "ờ": "owf",
    "ợ": "owj",
    "ở": "owr",
    "ỡ": "owx",
    "ú": "u.s",
    "ù": "u.f",
    "ủ": "u.r",
    "ụ": "u.j",
    "ũ": "u.x",
    "ư": "u.w",
    "ứ": "uws",
    "ừ": "uwf",
    "ử": "uwr",
    "ự": "uwj",
    "ữ": "uwx",
    "ý": "y.s",
    "ỳ": "y.f",
    "ỵ": "y.j",
    "ỹ": "y.x",
    "Á": "A.s",
    "À": "A.f",
    "Ạ": "A.j",
    "Ả": "A.r",
    "Ã": "A.x",
    "Ă": "A.w",
    "Ắ": "Aws",
    "Ằ": "Awf",
    "Ặ": "Awj",
    "Ẳ": "Awr",
    "Ẵ": "Awx",
    "Â": "A.a",
    "Ấ": "Aas",
    "Ầ": "Aaf",
    "Ậ": "Aaj",
    "Ẩ": "Aar",
    "Ẫ": "Aax",
    "É": "E.s",
    "È": "E.f",
    "Ẹ": "E.j",
    "Ẻ": "E.r",
    "Ẽ": "E.x",
    "Ê": "E.e",
    "Ế": "Ees",
    "Ề": "Eef",
    "Ệ": "Eej",
    "Ể": "Eer",
    "Ễ": "Eex",
    "Đ": "D.d",
    "Í": "I.s",
    "Ì": "I.f",
    "Ị": "I.j",
    "Ỉ": "I.r",
    "Ĩ": "I.x",
    "Ó": "O.s",
    "Ò": "O.f",
    "Ọ": "O.j",
    "Ỏ": "O.r",
    "Õ": "O.x",
    "Ô": "O.o",
    "Ố": "Oos",
    "Ồ": "Oof",
    "Ộ": "Ooj",
    "Ổ": "Oor",
    "Ỗ": "Oox",
    "Ơ": "O.w",
    "Ớ": "Ows",
    "Ờ": "Owf",
    "Ợ": "Owj",
    "Ở": "Owr",
    "Ỡ": "Owx",
    "Ú": "U.s",
    "Ù": "U.f",
    "Ủ": "U.r",
    "Ụ": "U.j",
    "Ũ": "U.x",
    "Ư": "U.w",
    "Ứ": "Uws",
    "Ừ": "Uwf",
    "Ử": "Uwr",
    "Ự": "Uwj",
    "Ữ": "Uwx",
    "Ý": "Y.s",
    "Ỳ": "Y.f",
    "Ỵ": "Y.j",
    "Ỹ": "Y.x",
}


def encode(message):
    encoded_string = b""
    for character in message:
        if character in alphabet.keys():
            encoded_character = alphabet[character]
        else:
            encoded_character = character
        encoded_string += bytes(encoded_character, encoding="utf-8")
    return encoded_string


def decode(message):
    decoded_string = ""
    chr_skip = 0
    for i in range(0, len(message)):
        i += chr_skip
        str3 = ''
        if i < len(message):
            character = chr(message[i])
            if i + 2 < len(message):
                str3 = character + chr(message[i + 1]) + chr(message[i + 2])
            if str3 in alphabet.values():
                decoded_character = get_key(str3)
                chr_skip += 2
            else:
                decoded_character = character
            decoded_string += decoded_character
        else:
            break

    return decoded_string


def get_key(val):
    for key, value in alphabet.items():
        if val == value:
            return key
