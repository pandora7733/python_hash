import hashlib

# 문자열 "Hello, world!"를 해시하는 예제
string = "Hello, world!"
hash_object = hashlib.sha256(string.encode()) # sha256 함수로 hash화, 문자열을 바이트로 변환
bite_dig = hash_object.digest() # 바이너리로 변환
hex_dig = hash_object.hexdigest() # 16진수로 변환

print("sha256, bite: ", bite_dig)
print("sha256, hex: ", hex_dig)