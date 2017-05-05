import random
import string


#Generate random 16 digit seed composed of lowercase, uppcase, and digits.
#Seed is combined with input phone number and used as seed for random
#A pseudo-random code is generated from this seed
def getCode(phoneNum): 
	seed = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
	random.seed(seed + phoneNum)
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)), seed

#Seed random using input seed and phoneNum
#Use to re-generate pseudo-random code
def recoverCode(seed, phoneNum):
	random.seed(seed + phoneNum)
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
