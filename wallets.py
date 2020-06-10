import hashlib
import datetime


class Wallets():
    ##PULLS 'name' STRING FROM 'wallet#' VARIABLE TO CREATE UNIQUE WALLET TRANSACTION##
    def __init__(self,name,balance=10):
        self.name=name
    ##FOW NOW TRANSACTION IS NESTED IN CLASS. WILL HAVE OWN FUNCTION##    
    def encrypt_trans(self):
        signature = hashlib.sha256(self.name.encode()).hexdigest()
        return signature
    def retun(self):
        encrypt_trans()
        print(signature)



wallet1 = Wallets('Clint')
wallet2=Wallets('Rashad')
wallet3=Wallets('Sean')
wallet4=Wallets('Satoshi')
wallet5=Wallets('Adnan')
wallet6=Wallets('Bob')
import_code=wallet1.encrypt_trans()
print(import_code)