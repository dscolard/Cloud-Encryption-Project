import os, io, sys

# Cryptography
from Crypto.Cipher import AES 
from Crypto import Random
from Crypto.Random import get_random_bytes

def genKey():
	key = get_random_bytes(16)
	file = open('key.key', 'wb')
	file.write(key)
	file.close()

def getKey():
	if os.path.getsize('key.key') > 0:
		file = open('key.key', 'rb')
		key = file.read()
		file.close()
		return key
	else:
		genKey()
		return getKey()

def encrypt(key, filename):
	filepath = "Test_Files/"+filename
	print("Encrypting..")
	chunksize = 64*1024
	outputFile = "(encrypted)"+filename
	filesize = str(os.path.getsize(filepath)).zfill(16)
	# Initialisation Vector
	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	with open(filepath, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)		
			while True:
				chunk = infile.read(chunksize)			
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))
				outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
	filepath = "Downloads/"+filename
	print("Decrypting..")
	chunksize = 64*1024
	outputFile = filename[11:]	
	with open(filepath, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)
		with open("Downloads/"+outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)



			