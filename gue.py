import datetime
import hashlib

class Block:
    block_id = 0
    trx = '0'
    next = None
    hash = None
    idx = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, trx):
        self.trx = trx

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.idx).encode() +
        str(self.trx).encode() +
        str(self.previous_hash).encode() +
        str(self.timestamp).encode() +
        str(self.block_id).encode()
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.block_id) + "\nBlock Data: " + str(self.trx) + "\nHashes: " + str(self.idx) + "\n--------------"

class ABCchain:

    diff = 20
    max_idx = 2**32
    target = 2 ** (256-diff)

    block = Block("First")
    hide = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.block_id = self.block.block_id + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.max_idx):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.idx += 1

ABCchain = ABCchain()

for n in range(1):
    ABCchain.mine(Block("Block " + str(n+1)))

while ABCchain.head != None:
    print(ABCchain.head)
    ABCchain.head = ABCchain.head.next