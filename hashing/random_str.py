import random
import hashlib
import time

en_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
en_high = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ko = ["ㅂ", "ㅃ", "ㄷ", "ㄸ", "ㄱ", "ㄲ", "ㅅ", "ㅆ", "ㅛ", "ㅕ", "ㅑ", "ㅐ", "ㅒ", "ㅔ", "ㅖ", "ㅁ", "ㄴ", "ㅇ", "ㄹ", "ㅎ", "ㅗ", "ㅓ", "ㅏ", "ㅣ", "ㅋ", "ㅌ", "ㅊ", "ㅍ", "ㅠ", "ㅜ", "ㅡ"]

string_low = random.choice(en_low)
string_high = random.choice(en_high)
string_ko = random.choice(ko)
num = str(random.randint(0, 255))

string = f"{string_low}{string_high}{string_ko}{num}"
print("원본 문자열:", string)

target_hash = hashlib.sha512(string.encode()).hexdigest()
print("목표 해시:", target_hash)

found = False
count = 0

start_time = time.time()

for i in en_low:
    for j in en_high:
        for k in ko:
            for l in range(0, 255):
                test_string = f"{i}{j}{k}{l}"
                hash_value = hashlib.sha512(test_string.encode()).hexdigest()
                count += 1

                if hash_value == target_hash:
                    print(f"\n 일치하는 문자열 발견: {test_string}")
                    print(f" 비교 횟수: {count}")
                    found = True
                    end_time = time.time()
                    elapsed = end_time - start_time
                    print(f"걸린 시간: {elapsed:.4f}초")
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print(f"\n 일치하는 문자열을 찾지 못함 (총 {count}회 시도)")