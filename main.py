import hashlib
import datetime
from wallets import Wallets

class Block:
    block_id = 0
    prev_block = None
    next_block=None
    confirm_tran=None
    info=None
    trx=None
    idx=0
    time=datetime.datetime.now

    ##INITIALIZES THE INFO FROM THE TRANSACTION##
    def __init__(self,info):
        self.info=info
       
    def c(self):
        h=hashlib.sha256()
        ##ADD NUMEROUS VARIABLES BELOW FROM PREVIOUS BLOCK TO DEEPEN CHAIN ECRYPTION##
        h.verify(
            str(self.block_id).encode() +
            str(self.prev_block).encode()+
            str(self.next_block).encode()+
            str(self.idx).encode+
            str(self.trx).encode()+
            str(self.info).encode())
        ##RETURNS THE ENCRYPTED HASH CODE##
        return h.hexdigest()


class Mychain:
    ##THIS FUNCTION HANDLES THE THE VALIDATION OF A TRANSACTION##
    dif_var = 10      ##ALLOWS US TO ADJUST THE DIFFICULTY OF SOLVING THE HASH##
    max_idx = 2**32
    ##BY LOWERING THE 'dif_var' WE ARE GIVING THE COMPUTER LESS ROOM TO CALC CORRECT HASH###
    chain_dif= 2**(256-dif_var)
    ##CREATES THE STARTING BLOCK OR 'GENESIS' BLOCK##
    block=Block('first')
    hide=head=block
    
    ##THIS FUNCTION CONNECTS THE CURRENT BLOCK TO THE NEXT ONE, SOLIDIFYING CHAIN ENCRYPTION##
    def link(self,block):
        block.prev_block=self.block.c() ##PREV. BLOCK SET TO CURRENT BLOCK##
        block.block_id= self.block.block_id += 1 ##CHANGE THE ID TO THE NEXT BLOCK##
        self.block.next_block=block 
        self.block= self.block.next_block
    
    ##THIS FUNCTION WILL ACT AS THE MINING FEATURE##
    def mining(self,block):
        for x in range(self.chain_dif):
            if int(block.c(),16) <=self.chain_dif:



 

