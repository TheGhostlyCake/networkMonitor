
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
	text.AddText("Ads Block: " + str(data['ads_blocked_today']) + "\r\n" + "hi" , 0, 20,15,  Id="ads" )
	text.AddText("DNS queries: " + str(data['dns_queries_today']), 0, 35,15, Id="dns" )
	text.AddText("Active Clients: " + str(data['unique_clients']), 0, 50,15, Id="clients" )
	text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

	

