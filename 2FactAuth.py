import sys
import os
from myCrypto import encrypt, decrypt
from rand import getCode, recoverCode
from sms import sendSms #(phoneNum, code)
import OpenSSL
import getpass

def TwoFactEncrypt():
	in_fileName = raw_input("Enter the name of the file to encrypt: ")
	in_file = open(in_fileName, 'rb') 

	# mid_file = open("intermediate", 'wb')

	out_fileName = raw_input("Enter the name of the output file: ")
	out_file = open(out_fileName, 'wb')

	password = getpass.getpass("Enter the password to set: ")
	password2 = getpass.getpass("Re-enter the password to set: ")

	if(password != password2):
		print("Passwords do not match, exiting.")
		sys.exit()
	else:
		print("Password accepted.")

	phoneNum = raw_input("Enter phone number for 2 factor authentication: ")

	print("Encrypting...")

	code, seed = getCode(phoneNum)

	mid_file = open("intermediate", 'wb')

	encrypt(in_file, mid_file, code)

	mid_file = open("intermediate", 'r+')


	mid_file.seek(0,2)		#navigate to the end of the file
	mid_file.write(seed)		#append seed to the end of the file
	mid_file.close()


	mid_file = open("intermediate", 'rb')

	encrypt(mid_file, out_file, password)

	mid_file.close()
	os.remove("intermediate")

	print("Encryption successful.")

	#Retrieved seed: sI83pu0mpPQaQnoG for phoneOut1.txt
	#Retrieved seed: dgxxef2F4hb5AUop for phoneOut2.txt
	#Retrieved seed: XiFDkbDQ2cWthjML for twoOut.txt

def TwoFactDecrypt():
	passed2 = 0
	print("Need to select twilio account for sending SMS, custom (free) account necessary for sending SMS to new phone number.")
	while(passed2 == 0):
		select = raw_input("Type 1 (Cecil's account) or 2 (custom account): ")
		if(select != '1' and select != '2'):
			print("Invalid input, please type '1' or '2'")
		else:
			passed2 = 1

	if(select == '1'):
		SID = "AC2ba203157ee8c7ad6231b397db9bc332"
		AUTH = "6bc073fc5f2b19988f1bcca5551f1981"
	else:
		SID = raw_input("Enter Twilio account SID: ")
		AUTH = raw_input("Enter Twilio account AUTH: ")

	in_fileName = raw_input("Enter the name of the file to decrypt: ")
	in_file = open(in_fileName, 'rb') 

	mid_file = open("intermediate", 'wb')

	out_fileName = raw_input("Enter the name of the output file: ")
	out_file = open(out_fileName, 'wb')

	password = getpass.getpass("Enter the password: ")

	phoneNum = raw_input("Enter the verified phone number: ")

	print("Decrypting...")

	decrypt(in_file, mid_file, password)

	mid_file.close()

	mid_file = open("intermediate", 'r+')

	mid_file.seek(0,2)
	size = mid_file.tell()
	mid_file.seek(size - 16)

	seed = mid_file.read(16)

	mid_file.truncate(size - 16)


	print("Sending verification code via sms...")

	sendSms(SID, AUTH, phoneNum, recoverCode(seed, phoneNum))

	userCode = raw_input("Enter the verification code: ")

	mid_file.close()

	mid_file = open("intermediate", 'rb')
	decrypt(mid_file, out_file, userCode)

	mid_file.close()
	os.remove("intermediate")

	print("Decryption complete.")



passed  = 0




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