#NOTE: Need to set environment variables TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN

#1 720-458-9327 

# import os

from twilio.rest import Client

# SID = os.getenv('TWILIO_ACCOUNT_SID')
# AUTH = os.getenv('TWILIO_AUTH_TOKEN')

TWILIO_ACCOUNT_SID = "AC2ba203157ee8c7ad6231b397db9bc332"
TWILIO_AUTH_TOKEN = "6bc073fc5f2b19988f1bcca5551f1981"
 
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
 
client.messages.create(from_='17204589327',
                       to='16304871267',
                       body='Ayy u wan sum fuk?')