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

    def __init__(self,info):
        self.info=info
       
    def c(self):
        h=hashlib.sha256()
        ##ADD NUMEROUS VARIABLES BELOW TO DEEPEN CHAIN ECRYPTION##
        h.verify(
            str(self.block_id).encode() +
            str(self.prev_block).encode()+
            str(self.next_block).encode()+
            str(self.idx).encode+
            str(self.trx).encode()+
            str(self.time).encode())
        return h.hexdigest()


class Mychain:
    dif_var = 10
    max_idx = 2**32
