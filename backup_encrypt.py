import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
        chunksize = 64*1024
        outputFile = "(encrypted)"+filename
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = ''

        for i in range(16):
                IV += chr(random.randint(0, 0xFF))

        encryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(filename, 'rb') as infile:
                with open(outputFile, 'wb') as outfile:
                        outfile.write(filesize)
                        outfile.write(IV)

                        while True:
                                chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
                                        break
                                elif len(chunk) % 16 != 0:
                                        chunk += ' ' * (16 - (len(chunk) % 16))

                                outfile.write(encryptor.encrypt(chunk))

def getKey(password):
        hasher = SHA256.new(password)
        return hasher.digest()

def Main():
		DB_HOST = 'localhost'
		DB_USER = 'root'
		DB_USER_PASSWORD = 'root'
		DB_NAME = 'flaskapp'
		db = DB_NAME
		dumpcmd = "mysqldump -u" + DB_USER + "-p" + DB_USER_PASSWORD + "" + db + ">" + "/" + db + ".sql"

		password = "root"
		filename = "flaskapp.sql"
		encrypt(getKey(password), filename)
                print "Done."

if __name__ == '__main__':
        Main()

