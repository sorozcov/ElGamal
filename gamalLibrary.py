# Universidad del Valle de Guatemala
# Cifrado de información 2020 2
# Grupo 7
# Implementation RSA.py

import random
from sympy import mod_inverse
from Crypto.Util.number import bytes_to_long ,long_to_bytes
import binascii

# First Alice and Bob will communicate thru RSA
# STEPS FOR RSA
# 1. Generate two big random prime number p and q
# 2. Calculate n = p*q
# 3. Use Euler Function φ of φ(n)=(p-1)(q-1) size
# Euler function gives all numbers between 1 and n with no common factors with n, it means are coprimes with n.
# 4. Pick a number e between 1 and φ(n) and also e is coprime with φ(n) and n
# 5. Calculate d knowing that e*d===1 mod φ(n)
# e is the public key (n,e)
# d is the private key (n,d)
