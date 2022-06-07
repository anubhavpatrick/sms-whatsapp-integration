'''
https://www.textlocal.in/free-developer-sms-api/
'''
 
import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message,  'test': 'true' })
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('NGI2YzU5NDYzOTc1Njk3NjMzNDMzODQyNTc0ZDc1NmU=', '+918447389366',
    'Anubha', 'Hi there, thank you for sending your first test message from Textlocal. See how you can send effective SMS campaigns here: https://tx.gl/r/2nGVj/')
print (resp)