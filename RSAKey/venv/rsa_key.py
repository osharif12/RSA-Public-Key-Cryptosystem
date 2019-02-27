# Omar Sharif, CS 683, RSA Public-Key Cryptosystem
'''
https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_understanding_rsa_algorithm.htm

'''

import random


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3 or num == 5:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    else:
        return True


p = random.randint(1, 10000)
q = random.randint(1, 10000)

while not is_prime(p):
    p = random.randint(1, 10000)

while not is_prime(q):
    q = random.randint(1, 10000)

# Generating the RSA modulus
n = p * q
print(p)
print(q)

p2 = p-1
q2 = q-1

# deriving a number e
e = q = random.randint(1, 10000)
flag = True;

while flag:
    e = q = random.randint(1, 10000)
    if e < p2 and e < q2 and is_prime(e):
        flag = False

print(e)

# (n, e) is the public key sent with user

# private key forumula: ed = 1 mod (p-1) (q-1)
d = (1 % (p2 * q2))/e
print(d)

# Encryption formula C = Pe mod n
enc = (p * e) % n
print(enc)

# Decryption formula: Plaintext = Cd mod n
dec = (enc * d) % n
print(dec)