import urllib3
from twilio.rest import Client
import SendGmail as sg

http = urllib3.PoolManager()

content = http.request(method="GET", url="https://www.lenovo.com/us/en/outletus/laptops/thinkpad/thinkpad-x-series/ThinkPad-X1-Carbon-5th-Gen/p/20HRX004US")

body = content.data.decode('UTF-8').lower()

if ("out  of stock" in body):
    print ('It is out of stock')
else:
    print ('It is in stock')
    sg.sendTMOSMS()
