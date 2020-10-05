# Universidad del Valle de Guatemala
# Cifrado de información 2020 2
# Grupo 7
# Implementación de El Gamal .py (sin librerías)

import random
import math

# calcula el máximo común denominador
def gcd( a, b ):
    while b != 0:
        c = a % b
        a = b
        b = c
        
    return a

# computa base^exp mod modulo
def modexp( base, exp, modulo ):
	return pow(base, exp, modulo)

# Alice
# simula al emisor de un mensaje en la implementación de ElGamal
class Alice(object):
    def __init__(self, public_key, gpk):
        self.mensaje_cifrado = []

        # obtenemos la llave pública de Bob
        self.public_key = public_key

        # se genera la llave privada de Alice (k)
        self._private_key = gpk(self.public_key['q'])

        # calculamos p - se devolverá con el mensaje cifrado
        self.p = modexp(self.public_key['g'], self._private_key, self.public_key['q'])

        print("VALORES COMPUTADOS POR ALICE")
        print("p (g^k) calculado: ", self.p)
        

    def cipher_message(self, mensaje):
        # calculamos s (g^ak) - s se mantiene secreto ya que Bob puede calcular s con p y su llave secreta
        s = modexp(self.public_key['h'], self._private_key, self.public_key['q'])

        for i in range(0, len(mensaje)):
            self.mensaje_cifrado.append(ord(mensaje[i]) * s)

        print("s (g^ak) calculado: ", s)

        return {
            'cifrado': self.mensaje_cifrado, 
            'p': self.p
        }

# Bob
# simula al receptor de un mensaje en la implementación de ElGamal
class Bob(object):
    def __init__(self):
        # mensaje descifrado
        self.mensaje_descifrado = []

    def generate_public_key(self, gpk):
        # se generan q y g, dos numeros grandes a ser usados en el cifrado
        self.q = random.randint(pow(10, 100), pow(10, 150))
        self.g = random.randint(2, self.q)
        print("LLAVE PÚBLICA DE BOB")
        print("q calculado: ", self.q)
        print("g elegido: ", self.g)

        # se genera la llave privada de Bob (a)
        self._private_key = gpk(self.q)

        # calculamos h (g^a)
        self.h = modexp(self.g, self._private_key, self.q)
        print("h (g^a) calculado: %i\n" % (self.h))

        return {
            'q': self.q,
            'g': self.g,
            'h': self.h
        }

    def decipher_message(self, mensaje_cifrado, p):
        # calculamos s nuevamente, esta vez utilizando p y a -> p^a = (g^k)^a = g^ak = s
        s = modexp(p, self._private_key, self.q)

        # se descifra el mensaje dividiéndolo por el valor s
        for i in range(0, len(mensaje_cifrado)):
            self.mensaje_descifrado.append(chr(int(mensaje_cifrado[i]/s)))

        # convertimos el mensaje descifrado en un único string 
        self.mensaje_descifrado = ''.join(self.mensaje_descifrado)

        # devolvemos el mensaje descifrado
        return self.mensaje_descifrado

# ElGamal
# simple implementación de un intercambio de mensajes por medio de la construcción ElGamal
# 
# Se recibe un mensaje de texto simple
# Se crea una instancia de Bob (receptor) y se genera la llave pública y privada
# Luego Alice utiliza esta llave pública para calcular p y s - s servirá para cifrar el mensaje
# Alice envía el mensaje cifrado y el valor p a Bob para que este lo descifre
# Bob calcula s con p y a 
# Bob descifra el mensaje utilizando s y puede leer el texto simple
class ElGamal(object):
    def __init__(self, m):
        # mensaje a original, cifrado y descifrado
        self.mensaje = m
        self.mensaje_cifrado = None
        self.mensaje_descifrado = []
        print("\nMensaje original: %s\n" % (m))

        # objeto Bob (receiver)
        self.bob = Bob()

        # almacenamos la llave pública
        self.public_key = self.bob.generate_public_key(self.generate_private_key)

        # objeto Alice (sender)
        self.alice = Alice(self.public_key, self.generate_private_key)

    
    # se genera la llave privada 
    def generate_private_key(self, q):
        key = random.randint(pow(10, 120), q)
        while gcd(q, key) != 1: 
            key = random.randint(pow(10, 120), q)
        
        return key

    # método para cifrado del mensaje
    def cifrar(self):
        self.mensaje_cifrado = self.alice.cipher_message(self.mensaje)

    # método para descifrar el mensaje
    def descifrar(self):
        self.mensaje_descifrado = self.bob.decipher_message(self.mensaje_cifrado['cifrado'], self.mensaje_cifrado['p'])
        
        return self.mensaje_descifrado

# 
# Llamamos a la clase e implementamos
#

mensaje = "Mensaje para cifrar con ElGamal"

elgamal = ElGamal(mensaje)

mensaje_cifrado = elgamal.cifrar()
mensaje_descifrado = elgamal.descifrar()

print("\nMensaje descifrado: %s\n" % (mensaje_descifrado))
