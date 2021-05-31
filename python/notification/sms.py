import requests
from datetime import datetime,date
import os


url = "https://www.fast2sms.com/dev/bulkV2"



def send_sms():
	now = datetime.now()
	today = date.today()

	d2 = today.strftime("%B %d, %Y")
	current_time = now.strftime("%H:%M:%S %p")

	txt = "Hi,\nTHI of cattle has rised above critical threshold. Counter Measures Activated Automatically.\nCounter Measures Activated at : "+d2+"  "+current_time+"\n\nFrom,\nTeam AHTM"

	payload = "sender_id=TXTIND&message="+txt+"&route=v3&numbers=7019750781"

	headers = {
	'authorization': os.environ['fast2sms_aut'],
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}

	response = requests.request("POST", url, data=payload, headers=headers)

	return response.text
