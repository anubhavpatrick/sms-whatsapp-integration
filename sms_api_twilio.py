'''
https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms?frameUrl=%2Fconsole%2Fsms%2Fapi-explorer%3Fx-target-region%3Dus1
'''

from twilio.rest import Client 
from credentials import AUTH_TOKEN, ACCOUNT_SID
 
client = Client(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.messages.create(       
                              body = 'Hello Madhu Darling. How are you!', 
                              to='+918447389366',
                              messaging_service_sid='MG95a3c61cd4d8fd5cd31c13c5760c6f56',
                          ) 
 
print(message.sid)