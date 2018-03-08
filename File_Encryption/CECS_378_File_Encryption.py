# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 12:43:47 2018

CECS 378 Project - File Encryption

@author: Michael Wolf & Chris Meyer
"""

"""
In this phase, you'll develop modules that will encrypt/decrypt a file.

I recommend using Python Cryptography (hazmat ONLY!). If you decide to use JS, there is vanilla JS lib at here. 
Should you have any questions regarding the crypto building blocks then do not hesitate to ask the instructor.

Make sure to use github to commit and push all of your code so the instructor can see your source.

You will design these modules:
"""
# IMPORTS
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

'''
#Code that we may use as a reference for syntax
backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message") + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()
'''
keyLength = 32
IVLength = 16
while(keyLength != 32):
    keyLength = int(input("Key must be 32 bytes, please enter in correct key length"))
    
#Generates a random key
key = os.urandom(keyLength)

def MyEncrypt(key, plaintext, associated_data):
    # Generate a random 96-bit IV.
    iv = GenerateIV()

    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    # associated_data will be authenticated but not encrypted,
    # it must also be passed in on decryption.
    encryptor.authenticate_additional_data(associated_data)

    # Encrypt the plaintext and get the associated ciphertext.
    # GCM does not require padding.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (iv, ciphertext, encryptor.tag)
    
def MyDecrypt(key, associated_data, iv, ciphertext, tag):
    # Construct a Cipher object, with the key, iv, and additionally the
    # GCM tag used for authenticating the message.
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    # We put associated_data back in or the tag will fail to verify
    # when we finalize the decryptor.
    decryptor.authenticate_additional_data(associated_data)

    # Decryption gets us the authenticated plaintext.
    # If the tag does not match an InvalidTag exception will be raised.
    return decryptor.update(ciphertext) + decryptor.finalize()

iv, ciphertext, tag = MyEncrypt (
    key,
    b"a secret message!",
    b"authenticated but not encrypted payload"
)

print(MyDecrypt(
    key,
    b"authenticated but not encrypted payload",
    iv,
    ciphertext,
    tag
))

""" PART 1
(C, IV)= Myencrypt(message, key):

In this method, you will generate a 16 Bytes IV, and encrypt the message using the key and IV in CBC mode (AES). 
You return an error if the len(key) < 32 (i.e., the key has to be 32 bytes= 256 bits).

(You'll have to write the inverse of the above methods.)
"""

def GenerateIV():
    iv =  os.urandom(IVLength) #random.
    
    return iv;

def MyEncrypt(message, key):
    result = ""
    iv = 1
    #random.rand
    #iv = Hazmat.primitives.ciphers.modes.CBC.initialization_vector
    print(iv)
    return result, iv;



#MyEncrypt("Test", "NotAKey")

def MyDecrypt(message, key, iv):
    result = ""
    
    return result;

#key = Fernet.generate_key()
#cipher_suite = Fernet(key)
#encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
#print(encoded_text)
#decoded_text = cipher_suite.decrypt(encoded_text)
#print(decoded_text)

""" PART 2
(C, IV, key, ext)= MyfileEncrypt (filepath):

In this method, you'll generate a 32Byte key. You open and read the file as a string.
You then call the above method to encrypt your file using the key you generated. 
You return the cipher C, IV, key and the extension of the file (as a string).

You'll have to write the inverse of the above methods. 

You will be asked to encrypt a JPEG file and then decrypt it and make sure you still can view the image.
"""



""" PART 3
Next, you will be asked to write a method as below:

(RSACipher, C, IV, ext)= MyRSAEncrypt(filepath, RSA_Publickey_filepath):

In this method, you first call MyfileEncrypt (filepath) which will return (C, IV, key, ext). 
You then will initialize an RSA public key encryption object and load pem publickey from the RSA_publickey_filepath. 
Lastly, you encrypt the key variable ("key") using the RSA publickey in OAEP padding mode. The result will be RSACipher. 
You then return (RSACipher, C, IV, ext). Remember to do the inverse (MyRSADecrypt (RSACipher, C, IV, ext, RSA_Privatekey_filepath)) 
which does the exactly inverse of the above and generate the decrypted file using your previous decryption methods.

Make sure to use github to commit and push all of your code so the instructor can see your source.
"""


