import sys
import os
from myCrypto import encrypt, decrypt
from rand import getCode, recoverCode

def TwoFactEncrypt():
	in_fileName = raw_input("Enter the name of the file to encrypt: ")
	in_file = open(in_fileName, 'rb') 

	mid_file = open("intermediate", 'wb')

	out_fileName = raw_input("Enter the name of the output file: ")
	out_file = open(out_fileName, 'wb')

	password = raw_input("Enter the password to set: ")

	password2 = raw_input("Re-enter the password to set: ")

	if(password != password2):
		print("Passwords do not match, exiting.")
		sys.exit()
	else:
		print("Password accepted.")

	phoneNum = raw_input("Enter phone number for 2 factor authentication: ")

	print("Encrypting...")

	code, seed = getCode(phoneNum)

	print("Retrieved seed: " + seed)

	encrypt(in_file, mid_file, code)

	mid_file = open("intermediate", 'wb')

	mid_file.seek(0)
	mid_file.write(seed)

	mid_file = open("intermediate", 'rb')

	encrypt(mid_file, out_file, password)



	# os.remove("intermediate")

	

	# print('Hello ' + person)
	print("Encryption successful.")

def TwoFactDecrypt():
	in_fileName = raw_input("Enter the name of the file to decrypt: ")
	in_file = open(in_fileName, 'rb') 

	mid_file = open("intermediate", 'wb')

	out_fileName = raw_input("Enter the name of the output file: ")
	out_file = open(out_fileName, 'wb')

	password = raw_input("Enter the password: ")

	phoneNum = raw_input("Enter the phone number: ")

	print("Decrypting...")

	decrypt(in_file, mid_file, phoneNum)

	mid_file = open("intermediate", 'rb')

	mid_file.seek(0)
	phoneNum = mid_file.read(10)
	# mid_file.seek(10)

	print("Read Phone Number = " + phoneNum)

	decrypt(mid_file, out_file, password)

	print("Decryption complete.")



passed = 0

while(passed == 0):
	select = raw_input("Type E (encrypt) or D (decrypt) ")

	if(select != 'E' and select != 'e' and select != 'd' and select != 'D'):
		print("Invalid input, please type 'E' or 'D'")
	else:
		passed = 1

if(select == "E" or select == "e"):
	TwoFactEncrypt()
else:
	TwoFactDecrypt()