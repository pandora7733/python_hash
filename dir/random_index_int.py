import random
import hashlib

# 계산 하는데 걸리는 시간 측정 (무작정 대입)

num = random.randint(0, 255)
binary = bin(num)[2:].zfill(8)

# hashing

str(binary) # 2진 8bit 수를 문자화
hash_object = hashlib.sha256(binary.encode())
hex_dig = hash_object.hexdigest()

print("hex : ", hex_dig)

result = hex_dig

# sha256으로 되어 있는 hex 값을 맞추기
for i in range(0, 255):
  binary_i = str(bin(i)[2:].zfill(8))
  hashing = hashlib.sha256(binary_i.encode())
  hex = hashing.hexdigest()
  print(hex)

  if result == hex:
    print("랜덤 숫자:", num)
    print("8비트 2진수:", binary)
    print("hex: ", hex)
    print("result: ", result)
    break
  else:
    continue