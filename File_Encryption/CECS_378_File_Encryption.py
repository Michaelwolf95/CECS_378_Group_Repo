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


""" PART 1
(C, IV)= Myencrypt(message, key):

In this method, you will generate a 16 Bytes IV, and encrypt the message using the key and IV in CBC mode (AES). 
You return an error if the len(key) < 32 (i.e., the key has to be 32 bytes= 256 bits).

(You'll have to write the inverse of the above methods.)
"""



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


