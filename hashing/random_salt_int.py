import random
import hashlib
import time

# 계산 하는데 걸리는 측정 (무작정 대입)

num = random.randint(0, 255)
binary1 = bin(num)[2:].zfill(8)
salt1 = random.randint(0, 255)

# hashing

str(binary1) # 2진 8bit 수를 문자화
str(salt1)
print("binary:", binary1)
print("salt:", salt1)

string = f"{binary1}{salt1}"
print("string:", string)

hash_object = hashlib.sha256(string.encode())
hex_dig = hash_object.hexdigest()
result = hex_dig
print("result:", result)

start_time = time.time() # 시작 시간

for i in range(0, 255):
  binary_i = str(bin(i)[2:].zfill(8))
  
  for j in range(0, 255):
    salt_i = str(j)
    test = f"{binary_i}{salt_i}"
    hash_test = hashlib.sha256(test.encode())
    hex_test = hash_test.hexdigest()
    if result == hex_test:
      print("hex_test:", hex_test)
      end_time = time.time() # 종료 시간
      elapsed = end_time - start_time
      print(f"걸린 시간: {elapsed:.4f}초")
      break
    else:
      continue
    

print("done")