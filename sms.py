from twilio.rest import Client

def sendSms(SID, AUTH, phoneNum, code):
	client = Client(SID, AUTH)
	 
	client.messages.create(from_='17204589327',
	                       to='1' + phoneNum,
	                       body='Decryption Code: ' + code)