from papirus import PapirusTextPos
import os, json, urllib3
import requests
import time
from time import gmtime, strftime

text = PapirusTextPos(rotation=0)


text.Clear()
text.AddText("NetMan:", 0, 0, Id="start" )

r = requests.get(url='http://10.0.0.95/admin/api.php')
data=r.json()
text.AddText("Ads Block: " + str(data['ads_blocked_today']), 0, 20,15,  Id="ads" )
text.AddText("DNS queries: " + str(data['dns_queries_today']), 0, 35,15, Id="dns" )
text.AddText("Active Clients: " + str(data['unique_clients']), 0, 50,15, Id="clients" )
text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

while(True):
	for x in range(0, 999):
		r = requests.get(url='http://10.0.0.95/admin/api.php')
		data=r.json()
		text.UpdateText("ads", "Ads Block: " + str(data['ads_blocked_today']))
		text.UpdateText("dns", "DNS queries: " + str(data['dns_queries_today']))
		text.UpdateText("clients", "Active Clients: " + str(data['unique_clients']))
		text.UpdateText("time", "time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		time.sleep(1)
	text.clear() 
	r = requests.get(url='http://10.0.0.95/admin/api.php')
	data=r.json()
	text.AddText("Ads Block: " + str(data['ads_blocked_today']), 0, 20,15,  Id="ads" )
	text.AddText("DNS queries: " + str(data['dns_queries_today']), 0, 35,15, Id="dns" )
	text.AddText("Active Clients: " + str(data['unique_clients']), 0, 50,15, Id="clients" )
	text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

	






# # Same as calling "PapirusTextPos(True [,rotation = rot])"
# text = PapirusTextPos(rotation=90)

# # Write text to the screen at selected point, with an Id
# # "hello world" will appear on the screen at (10, 10), font size 20, straight away
# text.AddText("hello world", 10, 10, Id="Start" )

# # Add another line of text, at the default location
# # "Another line" will appear on screen at (0, 0), font size 20, straight away
# text.AddText("Another line", Id="Top")

# # Update the first line
# # "hello world" will disappear and "New Text" will be displayed straight away
# text.UpdateText("Start", "New Text")

# # Remove The second line of text
# # "Another line" will be removed from the screen straight away
# text.RemoveText("Top")

# # Clear all text from the screen
# # This does a full update so is a little slower than just removing the text.
# text.Clear()
# def uptime:
# 	from datetime import timedelta
# # http://planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way
# 	with open('/proc/uptime', 'r') as f:
#     	uptime_seconds = float(f.readline().split()[0])
#     	uptime_string = str(timedelta(seconds = uptime_seconds))
# 	print(uptime_string)

# def connectiontype:
# 	response1 = os.system("ping -c 1 " +hostname1)
# 	response2 = os.system("ping -c 1 " +hostname2)
# 	response3 = os.system("ping -c 1 " +hostname3)
# 	response4 = os.system("ping -c 1 " +hostname4)

# 	if response1 == 0:
# 		print hostname, 'PiZero down!'
# 		text.write("PiZero WiFi Down!")
# 	else if response1 != 0 && response:
# 		print hostname, "WifiUp"
	
