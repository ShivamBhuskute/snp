import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

encryption_key = b"ABCDEFGHIJKLMNOP"
cipher_transformation = AES.MODE_CBC

def encrypt(plain_text):
    cipher = AES.new(encryption_key, cipher_transformation, iv=encryption_key)
    cipher_text = cipher.encrypt(pad(plain_text.encode("utf-8"), AES.block_size))
    return base64.b64encode(cipher_text).decode("utf-8")

def decrypt(encrypted_text):
    cipher = AES.new(encryption_key, cipher_transformation, iv=encryption_key)
    cipher_text = base64.b64decode(encrypted_text)
    return unpad(cipher.decrypt(cipher_text), AES.block_size).decode("utf-8")

plain_string = input("Enter String: ")

encrypted_string = encrypt(plain_string)
decrypted_string = decrypt(encrypted_string)

print("Plain String :", plain_string)
print("Encrypt String :", encrypted_string)
print("Decrypt String :", decrypted_string)
