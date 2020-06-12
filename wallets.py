import hashlib
import datetime




tx_amt= input('Input amount\:n')
class Wallets():
    ##PULLS 'name' STRING FROM 'wallet#' VARIABLE TO CREATE UNIQUE WALLET TRANSACTION##
    def __init__(self,name,balance):
        self.tx_amt=tx_amt
        #tx_amt= int(input('Input amount\:n'))
        self.name=name
        self.balance=balance
  
    ##THIS FUNCTION WILL CONFIRM THE EXCHANGE BETWEEN WALLETS AND BLOCKCHAIN##    
    def encrypt_trans(self):
        self.recip  = input('Who are you Sending to?\n')
        ha= hashlib.sha256()
        ha.update(
        str(self.tx_amt).encode() +
        str(self.balance).encode() + 
        str(self.)
        str(self.recip).encode())
        self.trans_id=ha.hexdigest()
        while True:
            from main import Block
            from main import ABCchain
            print('Your Transaction is being confirmed!\n\nTransaction ID: {}'.format(self.trans_id))
            break
            print(self.tx_amt)     
            if self.recip == 'Clint' or 'clint':
                self.balance -= int(self.tx_amt)
                wallet1.balance += int(self.tx_amt)
                print(wallet1.balance)


wallet1 = Wallets('Clint',10)
mywall=Wallets('User',10)

mywall.encrypt_trans()
#def transaction():


