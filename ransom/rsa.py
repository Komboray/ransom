from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

#############################################################
# STEP 1
# BELOW IS THE CODE THAT WE NEED FIRST TO EXECUTE IN ORDER TO GET THE FILES WITH THE KEYS
# WE HAVE COMMENTED THIS BELOW SECTION AS IT HAS BEEN USED
##############################################################
# key = RSA.generate(2048)
#
# private_key = key.export_key()
# with open('private.pem', 'wb')as f:
#     f.write(private_key)
#
# public_key = key.public_key().export_key()
# with open('public.pem', 'wb')as f:
#     f.write(public_key)


################################################################
# STEP 2
# print("> Encryption")
#
# public_key = RSA.import_key(open('public.pem').read())
#
# with open('fernet_key.txt', 'rb')as f:
#     fernet_key = f.read()
#
# #Public encrypter
# public_crypter = PKCS1_OAEP.new(public_key)
#
# # ENC THE SESSION KEY
# with open('enc_fernet_key.txt', 'wb')as f:
#     enc_fernet_key = public_crypter.encrypt(fernet_key)
#     f.write(enc_fernet_key)
#
# print(f'>Public key: {public_key}')
# print(f'>fernet key: {fernet_key}')
# print(f'>public crypter: {public_crypter}')
# print(f'>Encd fernet key: {enc_fernet_key}')
#
# print('> Enc completed\n')


########################################################################
# WE NEED TO RUN THE STEPS SEPARATELY AND COMMENT THEM OUT SEPARATELY
# STEP 3
with open('enc_fernet_key.txt', 'rb')as f:
    enc_fernet_key = f.read()

private_key = RSA.import_key(open('private.pem').read())

private_crypter = PKCS1_OAEP.new(private_key)

dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('dec_fernet_key.txt','wb') as f:
    f.write(dec_fernet_key)

print(f'>Public key: {private_key}')

print(f'>public crypter: {private_crypter}')
print(f'>Decd fernet key: {dec_fernet_key}')

print('> Dec completed\n')
