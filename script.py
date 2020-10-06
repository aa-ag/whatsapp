from twilio.rest import Client 
 
account_sid = 'AC285a73aa7ddb768392754249c53acea0' 
auth_token = '[AuthToken]' # from Twilio 
client = Client(account_sid, auth_token) 

def send_message():
    '''
    This functions sends the message thru Twilio
    It's called from clock.py
    '''
    message = client.messages.create( 
                                from_='whatsapp:+...', # phone number goes here  
                                body='I can send so much stuff from here!',      
                                to='whatsapp:+...' # recipient 
                            ) 
    
    print(message.sid)