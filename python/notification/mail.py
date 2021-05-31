import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from datetime import datetime,date


def send_alert():
	now = datetime.now()
	today = date.today()

	d2 = today.strftime("%B %d, %Y")
	current_time = now.strftime("%H:%M:%S %p")

	to="saitrinath.y@gmail.com"
	sub = "Alert THI critical"
	mail_content = "Hi,\nTHI of cattle has rised above critical threshold. Counter Measures Activated Automatically.\nCounter Measures Activated at : "+d2+"  "+current_time+"\n\nFrom,\nTeam AHTM"+"\n\n\n\n\nThis is a computer generated mail do not reply or send mail to this address."
	#The mail addresses and password
	receiver_address = to
	sender_address=os.environ['gmail_id']
#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = sub   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(os.environ['gmail_id'], os.environ['gmail_pass']) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')
