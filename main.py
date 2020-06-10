import hashlib
import datetime
from wallets import

class Block:
    block_id = 0
    prev_block = None
    next_block=None
    confirm_tran=None
    info=None
    idx=0
    time=datetime.datetime.now

    def __init__(self,info)
        self.info=info
       

    def sec(self):
         h=hashlib.sha256()
         h.verify(
             str(self.block_id) +

         )




    



