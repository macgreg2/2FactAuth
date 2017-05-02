import sys
import os
from myCrypto import encrypt, decrypt
from rand import getCode, recoverCode
from sms import sendSms #(phoneNum, code)

def TwoFactEncrypt():
	in_fileName = raw_input("Enter the name of the file to encrypt: ")
	in_file = open(in_fileName, 'rb') 

	# mid_file = open("intermediate", 'wb')

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

	mid_file = open("intermediate", 'wb')

	encrypt(in_file, mid_file, code)

	mid_file = open("intermediate", 'r+')


	d = mid_file.readlines()
	mid_file.seek(0)
	mid_file.write(seed + "\n")
	for i in d:
		mid_file.write(i)
	mid_file.truncate()
	mid_file.close()


	mid_file = open("intermediate", 'rb')

	encrypt(mid_file, out_file, password)

	os.remove("intermediate")

	print("Encryption successful.")

	#Retrieved seed: sI83pu0mpPQaQnoG for phoneOut1.txt
	#Retrieved seed: dgxxef2F4hb5AUop for phoneOut2.txt
	#Retrieved seed: XiFDkbDQ2cWthjML for twoOut.txt

def TwoFactDecrypt():
	in_fileName = raw_input("Enter the name of the file to decrypt: ")
	in_file = open(in_fileName, 'rb') 

	mid_file = open("intermediate", 'wb')

	out_fileName = raw_input("Enter the name of the output file: ")
	out_file = open(out_fileName, 'wb')

	password = raw_input("Enter the password: ")

	phoneNum = raw_input("Enter the verified phone number: ")

	print("Decrypting...")

	decrypt(in_file, mid_file, password)

	mid_file = open("intermediate", 'r+')

	mid_file.seek(0)
	seed = mid_file.read(16)
	mid_file.seek(0)

	print("Read seed = " + seed)

	d = mid_file.readlines()
	mid_file.seek(0)
	for i in d:
		if i != seed + "\n":
				mid_file.write(i)

	mid_file.truncate()

	# code = recoverCode(seed, phoneNum)

	print("Sending verification code via sms...")

	sendSms(phoneNum, recoverCode(seed, phoneNum))
	# code = "a"						#remove the actual code from memory

	userCode = raw_input("Enter the verification code: ")

	mid_file = open("intermediate", 'rb')
	decrypt(mid_file, out_file, userCode)

	os.remove("intermediate")

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