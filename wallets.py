import hashlib
import datetime


class Wallets():
    ##PULLS 'name' STRING FROM 'wallet#' VARIABLE TO CREATE UNIQUE WALLET TRANSACTION##
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    ##FOW NOW TRANSACTION IS NESTED IN CLASS. WILL HAVE OWN FUNCTION##    
    def encrypt_trans(self):
        signature = hashlib.sha256(self.name.encode()).hexdigest()
        return signature
    def retun(self):
        encrypt_trans()
        print(signature)



wallet1 = Wallets('Clint',10)
wallet2=Wallets('Rashad',10)
wallet3=Wallets('Sean',10)
mywall=Wallets('User',10)
import_code=wallet1.encrypt_trans()
print(import_code)

#def transaction():


