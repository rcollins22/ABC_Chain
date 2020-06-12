import datetime
import hashlib
#from wallets import Wallets


class Block:
    block_id = 0
    bkht = ''
    next = None
    hash = None
    idx = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    ##INITIALIZES THE INFO FROM THE TRANSACTION##
    def __init__(self, bkht):
        self.bkht = bkht      ##BLOCK HEIGHT##

    def hash(self):
        h = hashlib.sha256()
        ##ADD NUMEROUS VARIABLES BELOW FROM PREVIOUS BLOCK TO DEEPEN CHAIN ECRYPTION##
        h.update(
        str(self.idx).encode() +
        str(self.bkht).encode() +
        str(self.previous_hash).encode() +
        str(self.timestamp).encode() +
        str(self.block_id).encode())
        ##RETURNS THE ENCRYPTED HASH CODE##
        #h.hexdigest()=trans_id
        print(str(h.hexdigest()))
        return h.hexdigest()

#     def __str__(self):
#         return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.block_id) + "\nBlock Data: " + str(self.bkht) + "\nHashes: " + str(self.idx) + "\n--------------"

# class ABCchain:
#         ##THIS FUNCTION HANDLES THE THE VALIDATION OF A TRANSACTION##
#     diff = 15      ##ALLOWS US TO ADJUST THE DIFFICULTY OF SOLVING THE HASH##
#     max_idx = 2**32
#     target = 2 ** (256-diff)
#     ##CREATES THE STARTING BLOCK OR 'GENESIS' BLOCK##
#     block = Block("First")
#     ##ALLOWS THE VARIABLES TO NOT CONSTANTLY BE SET TO EACH OTHER, FOR A 'not' LOOP LATER##
#     hide = head = block

#     ##THIS FUNCTION CONNECTS THE CURRENT BLOCK TO THE NEXT ONE, SOLIDIFYING CHAIN ENCRYPTION##
#     def add(self, block):

#         block.previous_hash = self.block.hash() ##PREV. BLOCK SET TO CURRENT BLOCK##
#         block.block_id = self.block.block_id + 1  ##CHANGE THE ID TO THE NEXT BLOCK##

#         self.block.next = block     ##VARIABLE CREATED FOR THE NEXT BLOCK##
#         self.block = self.block.next     ##CONTINUALLY SETS THE NEXT BLOCK HASH##

#     ##THIS FUNCTION WILL ACT AS THE MINING FEATURE##
#     def mining(self, block):
#         for n in range(self.max_idx):
#             if int(block.hash(), 16) <= self.target:
#                 self.add(block)
#                 print(block)
#                 break
#             else:
#                 block.idx += 1
# success = True

# ABCchain = ABCchain()

# for n in range(3):
#     ABCchain.mining(Block("Block " + str(n+1)))

# while ABCchain.head != None:
#     #print(ABCchain.head)
#     ABCchain.head = ABCchain.head.next