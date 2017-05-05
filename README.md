# 2FactAuth
Cecil Macgregor - macgreg2 - UIUC CS 460 

Python script and .exe designed to encrypt/decrypt arbitrary files on a windows machine using two-factor authentication.

Free online SMS service Twilio (https://twilio.com) is utilized to send verification test. Requires internet connection and a free account. 

Methodology: A phone number, password and random code are used to encrypt a selected file. Decryption requires knowledge of the password and entering the random code which is texted to the user, ensuring two factor authentication through something you know (the password) and something you have (the phone number). 

The python source code is provided (2FactAuth.py), along with a folder (2FactAuthExe) which contains the executable (2FactAuth.exe) and supporting files. Intended use is with the executable only, which yields a number of benefits:

  1) The user do not need to have python installed on their system, nor do they need to understand how python scripts work, allowing for ease of use among the computer illiterate populace.
  2) The (possibly hostile) users cannot read the source code and must use a dissasembler to examine it, raising the difficulty level for those who may try to exploit the code.
  3) The executable's support files found in 2FactAuthExe\ bundles in the third party python modules used, so they don't have to be set up on the users system. It's as easy as point and click.

Usage: Simply download and extract the 2FactAuthExe folder, and run the 2FactAuth.exe found within. Usage is intuitive, with the user being queried whether they would like to encrypt or decrypt. 

  Encryption: The user will be asked
  1) The name or path of the file to be encrypted.
  2) The desired name or path for the encrypted output file.
  3) A password.
  4) A phone number (this must match the phone number used to decrypt the file).

Decryption: The user will be asked
  1) For a Twilio account SID and AUTH. 
  2) The name or path of the file to by decrypted.
  3) The desired name or path for the decrypted output file.
  4) A password.
  5) The phone number associated with the file to be decrypted.
