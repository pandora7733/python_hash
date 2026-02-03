import hashlib

string = input("hashing: ")
hash_object = hashlib.sha256(string.encode()) # 입력된 문자를 해싱, 무자열을 바이트로 변환
hex_dig = hash_object.hexdigest() # 16진수로 변환

print("sha256, hex: ", hex_dig)