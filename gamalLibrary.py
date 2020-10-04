# Universidad del Valle de Guatemala
# Cifrado de información 2020 2
# Grupo 7
# Implementation El Gamal .py

#We import el gamal library
from elgamal.elgamal import Elgamal

print("This is an example of el gamal cipher using elgamal python library.")
message = b'My Secret Message'
print("The message Alice wants to send Bob is: ", message)

# Based on Taher Elgamal discrete logarithm being one way functions
# We generate the keys needed with a big random prime number P
# We also calculate a primitive root for P alfa.
# We then choose a number between 1 and P, known as Lambda

# Lambda will be our private key
# The public key will be composed by P and the primitive root, being beta=alfa^lambda mod p
publicKey, privateKey = Elgamal.newkeys(128)

print("The public key will be: ", publicKey)
print("The private key will be: ", privateKey)

#We encrypt the message using the publicKey
# To encrypt the message Alice generates a random number U
# And uses Bob public key that has p,alfa to encrypt the message
# Then from the operation only Bob with privateKey will be able to decrypt
# N1 = G^U
# N2 = M*S
# N2*m_-1=S
encypted = Elgamal.encrypt(message, publicKey)
print("Encrypted Message: ", encypted)

#The wen can only decrypt the message if we know the privateKey x
# S=N1^x
# S-1= S*N1^(q-x)
# N2*S-1=m
decrypted = Elgamal.decrypt(encypted, privateKey)
print("Decrypted Message: ", decrypted)
