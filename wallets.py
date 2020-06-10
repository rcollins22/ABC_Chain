import hashlib
import datetime


class Wallets():

    def __init__(self,name,balance=10):
        self.name=name
        
    def encrypt_trans(self):
        signature = hashlib.sha256(self.hash_string.encode()).hexdigest()
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
#import_code=my_wallet.encrypt_trans()
#print(import_code)