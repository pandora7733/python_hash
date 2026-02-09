import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain(object):

  def __init__(self):
    self.chain = []
    self.current_transactions = []

    self.new_block(previous_hash=1, proof=100) # genesis block 첫번쨰 생성될 블록

  def new_block(self, proof, previous_hash=None):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1])
    }

    self.current_transactions = []
    self.chain.append(block)

    return block

  def new_transaction(self, sender, recipient, amount):
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })
    
    return self.last_block['index']+1

  @staticmethod # staticmethod 정적 메소드를 사용하여 self인자 없이, 입력 받은 데이터만 암호화 하여 반환
  def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  @property # property 데코레이터를 사용하여 데이터 그 자체 처럼 취급 -> 보다 직관적임 (이유: 마지막 조회 작업 이기 때문!)
  def last_block(self):
    return self.chain[-1]
  
  def proof_of_work(self, last_proof, last_hash):

    proof = 0

    while self.valid_proof(last_proof, proof, last_hash) is False:
      proof += 1

    return proof
  
  @staticmethod
  # 실제 블록체인의 해시 생성 방식
  # sha256(sha256(이전 블록의 해시, 머클 루트, 타임스탬프, 난이도 목표, 버전, 논스))
  # def valid_proof(last_proof, proof):
  #   guess = str(last_proof * proof).encode()
  #   guess_hash = hashlib.sha256(guess).hexdigest()
  #   return guess_hash[:4] == "0000"
  def valid_proof(last_proof, proof, last_hash):
    guess = f'{last_proof}{proof}{last_hash}'.encode() # 반복되던 proof값 수정
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"