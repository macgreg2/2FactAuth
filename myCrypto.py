# USAGE:
# with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
#     encrypt(in_file, out_file, password)
# with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
#     decrypt(in_file, out_file, password)


from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random
from rand import getCode, recoverCode

def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = ''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]

def encrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = Random.new().read(bs - len('Salted__'))
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_file.write('Salted__' + salt)
    finished = False
    while not finished:
        chunk = in_file.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = bs - (len(chunk) % bs)
            chunk += padding_length * chr(padding_length)
            finished = True
        out_file.write(cipher.encrypt(chunk))

def decrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = in_file.read(bs)[len('Salted__'):]
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            if padding_length < 1 or padding_length > bs:
               raise ValueError("bad decrypt pad (%d)" % padding_length)
            # all the pad-bytes must be the same
            if chunk[-padding_length:] != (padding_length * chr(padding_length)):
               # this is similar to the bad decrypt:evp_enc.c from openssl program
               raise ValueError("bad decrypt")
            chunk = chunk[:-padding_length]
            finished = True
        out_file.write(chunk)

# def derive_key_and_iv(password, salt, key_length, iv_length):
#     d = d_i = ''
#     while len(d) < key_length + iv_length:
#         d_i = md5(d_i + password + salt).digest()
#         d += d_i
#     return d[:key_length], d[key_length:key_length+iv_length]

# def encrypt(in_file, out_file, password, key_length=32):
#     bs = AES.block_size
#     salt = Random.new().read(bs - len('Salted__'))
#     key, iv = derive_key_and_iv(password, salt, key_length, bs)
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     out_file.write('Salted__' + salt)
#     finished = False
#     while not finished:
#         chunk = in_file.read(1024 * bs)
#         if len(chunk) == 0 or len(chunk) % bs != 0:
#             padding_length = (bs - len(chunk) % bs) or bs
#             chunk += padding_length * chr(padding_length)
#             finished = True
#         out_file.write(cipher.encrypt(chunk))

# def decrypt(in_file, out_file, password, key_length=32):
#     bs = AES.block_size
#     salt = in_file.read(bs)[len('Salted__'):]
#     key, iv = derive_key_and_iv(password, salt, key_length, bs)
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     next_chunk = ''
#     finished = False
#     while not finished:
#         chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
#         if len(next_chunk) == 0:
#             padding_length = ord(chunk[-1])
#             chunk = chunk[:-padding_length]
#             finished = True
#         out_file.write(chunk)


password = "pancake"
phoneNum = "3036181122"
code, seed = getCode(phoneNum)
from shutil import copyfile
# ENCRYPT----------------------------------------

with open("in.jpg", 'rb') as in_file, open("testOut", 'wb') as out_file:
    encrypt(in_file, out_file, code)
    copyfile("testOut", "testOutCopy")



out_file = open("testOut", 'r+')


out_file.seek(0,2)              #navigate to the end of the file
out_file.write(seed)
out_file.close()

with open("testOut", 'rb') as in_file, open("testOut2", 'wb') as out_file:
    encrypt(in_file, out_file, password)


#DECRYPT-----------------------------------------


with open("testOut2", 'rb') as in_file, open("testOut3", 'wb') as out_file:
    decrypt(in_file, out_file, password)


out_file = open("testOut3", 'r+')

out_file.seek(0,2)
size = out_file.tell()
out_file.seek(size - 16)

seed = out_file.read(16)

out_file.truncate(size - 16)




# with open("testOut3", 'rb') as out_file:
#     for line in out_file:
#         if not line.strip():
#             break
#     open("testOutNew", 'wb').writelines(out_file)


# d = out_file.readlines()
# out_file.seek(0)
# for i in d:
#     # print(out_file.tell())
#     if i != seed + "\n":
#         out_file.write(i)

# location = out_file.tell()

# print("Current pointer location: ")
# print(location)

# print("Size - location: ")
# print(size-location)

# out_file.truncate(size - (size-location))

out_file.close()
code = recoverCode(seed, phoneNum)

with open("testOut3", 'rb') as in_file, open("testOut.jpg", 'wb') as out_file:
    decrypt(in_file, out_file, code)