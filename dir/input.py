import hashlib

M = input("hashing: ")
hash_object = hashlib.sha256(M.encode())
hex_dig = hash_object.hexdigest()

print("sha256, hex: ", hex_dig)