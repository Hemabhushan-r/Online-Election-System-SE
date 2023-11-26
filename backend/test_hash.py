import hashlib
salt = 123456
password = 'test'
hashed_password = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode("utf-8"),
    str(salt).encode("utf-8"),
    100000
)
print(str(hashed_password))
