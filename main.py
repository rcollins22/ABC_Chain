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
    dif_var = 10
    max_idx = 2**32
    chain_dif= 2**(256-dif_var)
    ##CREATES THE STARTING BLOCK OR 'GENESIS' BLOCK##
    block=Block('first')
    hide=head=block
    
    ##THIS FUNCTION CONNECTS THE CURRENT BLOCK TO THE NEXT ONE, SOLIDIFYING CHAIN ENCRYPTION##
    def link(self,block):
        block.prev_block=self.block.c()
        block.block_id= self.block.block_id += 1
        self.block.next_block=block
        self.block= self.block.next_block
    
    def mining(self, )

 

