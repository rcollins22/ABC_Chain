import hashlib
import datetime


class Wallets():

    def __init__(self,balance=10):
        self.hash_string=hash_string
        
    def encrypt_trans(self):
        signature = hashlib.sha256(self.hash_string.encode()).hexdigest()
        return signature
    def retun(self):
        encrypt_trans()
        print(signature)



1wallet=Wallets('Clint')
2wallet=Wallets('Rashad')
3wallet=Wallets('Sean')
4wallet=Wallets('Satoshi')
5wallet=Wallets('Adnan')
6wallet=Wallets('Bob')
#import_code=my_wallet.encrypt_trans()
#print(import_code)