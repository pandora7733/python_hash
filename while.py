import hashlib

while True:
  M = input("hashing: ")

  if type(M) == str:
    if M == 0:
      print("stop hashing")
      break
    else:
      str(M)
      hash_object = hashlib.sha256(M.encode())
      hex_dig = hash_object.hexdigest()
      print(hex_dig)
      continue
  else:
    hash_object = hashlib.sha256(M.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    continue

