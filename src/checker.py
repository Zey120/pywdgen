# https://xposedornot.com/
import json
import urllib3
from hasher import Keccak512


# We can now control the number of todos we want to be returned.
def check(password):
    hashed_password = Keccak512(password)
    print(hashed_password)
    http = urllib3.PoolManager()
    r = http.request("GET", f"https://passwords.xposedornot.com/api/v1/pass/anon/{hashed_password}")
    print(r.data)
    if r.data != b'{"Error":"Not found"}\n':
        print(type(r.data))


check("password")
