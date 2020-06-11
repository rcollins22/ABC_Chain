import hashlib
import datetime


tx_amt= float(input('Input amount\:n'))
class Wallets():
    ##PULLS 'name' STRING FROM 'wallet#' VARIABLE TO CREATE UNIQUE WALLET TRANSACTION##
    def __init__(self,name,balance):
        self.tx_amt=2
        #tx_amt= int(input('Input amount\:n'))
        self.name=name
        self.balance=balance
        #print(self.balance)
    # my_bal=balance
    # print(my_bal)
    recip  = input('Who are you Sending to?\n')

    
    # print(wallet1)
    ##FOR NOW TRANSACTION IS NESTED IN CLASS. WILL HAVE OWN FUNCTION##    
    def encrypt_trans(self):
        #print(wallet1)
        ha= hashlib.sha256()
        ha.update(
        str(self.tx_amt).encode() +
        str(self.balance).encode() +
        str(self.recip).encode())
        self.trans_id=ha.hexdigest()

        print('Your Transaction is being confirmed!\n\nTransaction ID: {}'.format(self.trans_id))

    def cond_trans(self):
        while confirmed != True:
            if self.recip == 'Clint' or 'clint':
                self.balance -= self.tx_amt
                wallet1.balance += self.tx_amt
                print(wallet1.balance)

    cond_trans()
            

    def retun(self):
        signature=self.encrypt_trans()
        print(signature)
    





wallet1 = Wallets('Clint',10)
wallet2=Wallets('Floyd',10)
wallet3=Wallets('Sean',10)
mywall=Wallets('User',10)
wallet1.retun()


#def transaction():


