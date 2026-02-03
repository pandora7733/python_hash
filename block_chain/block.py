# 블록 예시

block = {
    'index': 1, # 몇 번쨰 블록
    'timestamp': 1506057125.900785, # UNIX TIME을 기준으로 한 블록의 생성 시간
    'transactions': [ # 블록에 넣을 데이터
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00", # 보내는 사람
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f", # 받는 사람
            'amount': 5, # 양
        }
    ],
    'proof': 324984774000, # 작업증명 결과
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" # 이전 블록의 번호
}