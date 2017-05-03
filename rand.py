import random
import string

def getCode(phoneNum):
	seed = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
	random.seed(seed + phoneNum)
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16)), seed

def recoverCode(seed, phoneNum):
	random.seed(seed + phoneNum)
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

# while(1):
# 	seed = raw_input("Enter the desired seed: ")
# 	random.seed(seed)
# 	# for i in range(0,10):
# 	# 	print(random.randint(1000000,9999999))
# 	randPass = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
# 	print(randPass)