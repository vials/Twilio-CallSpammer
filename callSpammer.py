import sys
from twilio.rest import Client
import subprocess as sp
from colorama import Fore, init
init()

numberRegionCode = '+1' #Can modify this to whatever, just make sure to edit the GET request
client = Client('<ACCOUNT SID>', '<AUTH TOKEN>')
callInstructions = 'http://static.fullstackpython.com/phone-calls-python.xml'

banner = Fore.GREEN+'''
 .d8888b.           888 888
d88P  Y88b          888 888
888    888          888 888
888         8888b.  888 888
888            "88b 888 888
888    888 .d888888 888 888
Y88b  d88P 888  888 888 888
 "Y8888P"  "Y888888 888 888
 .d8888b.
d88P  Y88b
Y88b
 "Y888b.   88888b.   8888b.  88888b.d88b.  88888b.d88b.   .d88b.  888d888
    "Y88b. 888 "88b     "88b 888 "888 "88b 888 "888 "88b d8P  Y8b 888P"
      "888 888  888 .d888888 888  888  888 888  888  888 88888888 888
Y88b  d88P 888 d88P 888  888 888  888  888 888  888  888 Y8b.     888
 "Y8888P"  88888P"  "Y888888 888  888  888 888  888  888  "Y8888  888
           888
           888
           888
'''+Fore.WHITE
bannerCreds = 'Created By '+Fore.CYAN+'Inc'+Fore.WHITE
def main():
	clear()
	print(banner+bannerCreds+'\n')
	twilioNumber = raw_input(Fore.GREEN+'Please Enter Your Twilio Number: '+Fore.RED)
	numberToDial = raw_input(Fore.GREEN+'Please Enter Number To Call: '+Fore.RED)
	numberToSpam = raw_input(Fore.GREEN+'Please Enter Amount Of Times To Call: '+Fore.RED)

	try:
		for i in range(int(numberToSpam)):
			#print(Fore.WHITE+'Calling '+numberToDial+' '+str(i+1)+' Times')
			msg = (Fore.WHITE+'Calling {} {} Times'.format(numberToDial, str(i+1)))
			sys.stdout.write("\r{:<90}".format(msg))
			sys.stdout.flush()
			client.calls.create(to=numberRegionCode+numberToDial, 
				from_=numberRegionCode+twilioNumber, 
				url=callInstructions, 
				method='GET')
	except Exception as e:
		pass
		if "Trial accounts may only make calls to verified numbers." in e:
			print('Trial Accounts Can Only Call Verified Numbers')
		else:
			'''Do 
				Nothing'''
		print(str(e))
	print(Fore.GREEN+'Done!'+Fore.WHITE)

def clear():
	sp.call('clear', shell=True)

if __name__ == '__main__':
	main()
  
'''
Ensure you leave credits if you wish you use this script. Credits are nice and any dev likes that!
Enjoy.
'''
