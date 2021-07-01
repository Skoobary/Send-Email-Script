import smtplib
from email.mime.text import MIMEText        #Imports
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
body = 'This is the body of the email.' #Email's body
body = MIMEText(body) # convert the body to a MIME compatible string
msg.attach(body) # attach it to your main message
msg['From'] = 'from_emai@gmail.com' #Email author's address
msg['To'] = 'to_email@gmail.com' #Destination address
msg['Subject'] = 'OMG Super Important Message' #Email's subject

def send_email(): # This function sends an email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #SMTP Server
        server.ehlo()
        server.login("from_email@gmail.com", "Password_HERE") #Logs in to account using credentials
        server.sendmail(msg['From'], msg['To'], msg.as_string()) #Sends email with anterior parameters
        server.close() #Closes connection
        print("Message successfully Sent!") #Prints out State
    except:
        print('Something went wrong...') # Prints out State

if __name__ == '__main__':
    send_email()
