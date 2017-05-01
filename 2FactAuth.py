import sys
from myCrypto import encrypt, decrypt

in_fileName = raw_input("Enter the name of the file to encrypt: ")
in_file = open(in_fileName, 'rb') 

out_fileName = raw_input("Enter the name of the output file: ")
out_file = open(out_fileName, 'wb')

password = raw_input("Enter the password to set: ")

password2 = raw_input("Re-enter the password to set: ")

if(password != password2):
	print("Passwords do not match, exiting.")
	sys.exit()
else:
	print("Password accepted.")
	encrypt(in_file, out_file, password)

print("Encrypting...")

# print('Hello ' + person)
print("Script ended.")