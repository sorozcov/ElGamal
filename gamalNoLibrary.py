# Universidad del Valle de Guatemala
# Cifrado de información 2020 2
# Grupo 7
# Implementation El Gamal .py (sin librerias)

import random
import math

# calcula el maximo comun denominador
def gcd( a, b ):
    while b != 0:
        c = a % b
        a = b
        b = c
        
    return a

# computa base^exp mod modulo
def modexp( base, exp, modulo ):
	return pow(base, exp, modulo)

class ElGamal(object):
    def __init__(self, m):
        # mensaje a original, cifrado y descifrado
        self.mensaje = m
        self.mensaje_cifrado = []
        self.mensaje_descifrado = []
        print("\nMensaje original: %s\n" % (m))

        # primer paso - Bob genera una llave pública y una llave privada
        # la llave privada se almacena para descifrar el mensaje entrante
        self.generate_bob()

        # segundo paso - Alice realiza la encripción del mensaje con la llave pública
        self.generate_alice()

    def restart(self, m):
        self.__init__(m)

    # generamos q, g, a y h
    def generate_bob(self):
        # se generan q y g, dos numeros grandes a ser usados en la encripcion
        self.q = random.randint(pow(10, 100), pow(10, 150))
        self.g = random.randint(2, self.q)
        print("LLAVE PÚBLICA DE BOB")
        print("q calculado: ", self.q)
        print("g calculado: ", self.g)

        # se genera la llave privada de Bob (a)
        self.bob_private_key = self.generate_private_key()

        # calculamos h (g^a)
        self.h = modexp(self.g, self.bob_private_key, self.q)
        print("h (g^a) calculado: %i\n" % (self.h))

    # se genera la llave privada de alice y se computan s y p. p se publica, s se mantiene secreto
    def generate_alice(self):
        # se genera la llave privada de Alice (k)
        self.alice_private_key = self.generate_private_key()

        # calculamos s y p - s se mantiene secreto, p se devuelve con el mensaje cifrado
        s = modexp(self.h, self.alice_private_key, self.q)
        self.p = modexp(self.g, self.alice_private_key, self.q)
        print("VALORES COMPUTADOS POR ALICE")
        print("p (g^k) calculado: ", self.p)
        print("s (g^ak) calculado: ", s)
        
        # ciframos el mensaje utilizando s
        self.cifrar(s)
    
    # se genera la llave privada 
    def generate_private_key(self):
        key = random.randint(pow(10, 120), self.q)
        while gcd(self.q, key) != 1: 
            key = random.randint(pow(10, 120), self.q)
        
        return key

    # método para cifrado del mensaje
    def cifrar(self, s):
        for i in range(0, len(self.mensaje)):
            self.mensaje_cifrado.append(ord(self.mensaje[i]) * s)

    # método para descifrar el mensaje
    def descifrar(self):
        # calculamos s nuevamente, esta vez utilizando p y a -> p^a = (g^k)^a = g^ak = s
        s = modexp(self.p, self.bob_private_key, self.q)

        # se descifra el mensaje dividiendolo por el valor s
        for i in range(0, len(self.mensaje_cifrado)):
            self.mensaje_descifrado.append(chr(int(self.mensaje_cifrado[i]/s)))

        # convertimos el mensaje descifrado en un único string 
        self.mensaje_descifrado = ''.join(self.mensaje_descifrado)

        # devolvemos el mensaje descifrado
        return self.mensaje_descifrado


# 
# Llamamos a la clase e implementamos
#

mensaje = "Mi mensaje secreto"

elgamal = ElGamal(mensaje)

mensaje_descifrado = elgamal.descifrar()
print("\nMensaje descifrado: %s\n" % (mensaje_descifrado))