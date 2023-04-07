from Crypto.Hash import keccak
import hashlib

k = keccak.new(digest_bits=512)
k.update(b'test')
print(k.hexdigest())
print(type(k))

def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8'))
    print(HashedPassword)