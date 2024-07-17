from cryptography.fernet import Fernet

################################################################
# STEP 1 ENCRYPTION
# key = Fernet.generate_key()
#
# crypter = Fernet(key)
#
# with open('fernet_key.txt','wb')as f:
#     f.write(key)
#
# with open('ransom.jpg', 'rb')as f:
#     data = f.read()
#     with open('enc_pic.jpg', 'wb')as f:
#         cryp_data = crypter.encrypt(data)
#         f.write(cryp_data)
#
#     print('encd...')

###############################################################
# STEP 2
#
with open('fernet_key.txt','r')as f:
    key = f.read()
crypter = Fernet(key)

with open('enc_pic.jpg', 'rb')as f:
    data = f.read()

with open('dec_pic.jpg', 'wb')as f:
    decryp_data = crypter.decrypt(data)
    f.write(decryp_data)

    print('decd...')