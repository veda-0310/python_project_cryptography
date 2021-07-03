from cryptography.fernet import Fernet
def writeKey():
  key = Fernet.generate_key()
  with open('mykey.key','wb')as mykey:
    mykey.write(key)

def loadKey():
    return open('mykey.key','rb').read()

def enc(key):
    print(key)

    fer = Fernet(key)
    with open('students.txt', 'rb')as originalFile:
       original = originalFile.read()
    encrypted = fer.encrypt(original)
    with open('students1.txt', 'wb')as encryptedFile:
            encryptedFile.write(encrypted)

def dec(key):
    fer = Fernet(key)

    with open('students1.txt', 'rb')as encryptedFile:
         encrypted = encryptedFile.read()
    decrypted = fer.decrypt(encrypted)
    with open('students2.txt', 'wb')as decryptedFile:
        decryptedFile.write(decrypted)


