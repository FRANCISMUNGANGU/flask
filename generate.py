import os
# generate the secret key
myKey = os.urandom(24).hex()
print(myKey)
