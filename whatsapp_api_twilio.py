from twilio.rest import Client 
from credentials import AUTH_TOKEN, ACCOUNT_SID
 
client = Client(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello Madhu Darling. How are you!',      
                              to='whatsapp:+918447389366' 
                          ) 
 
print(message.sid[AUTH_TOKEN])