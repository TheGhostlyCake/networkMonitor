
from papirus import PapirusTextPos
import os, json, urllib3
import requests
import time
from time import gmtime, strftime

text = PapirusTextPos(rotation=0)


text.Clear()
text.AddText("NetMan:", 0, 0, Id="start" )



while(True):
	r = requests.get(url='http://10.0.0.95/admin/api.php')
	data=r.json()
	text.AddText("Ads Block: " + str(data['ads_blocked_today']) +"\r\n" + "DNS queries: " + str(data['dns_queries_today)'] + "\r\n" + "Active Clients: " + str(data['unique_clients']) , 0, 20,15,  Id="main" )
	text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

	for x in range(0, 999):
		r = requests.get(url='http://10.0.0.95/admin/api.php')
		data=r.json()
		text.UpdateText("main", "Ads Block: " + str(data['ads_blocked_today']) +"\r\n" + "DNS queries: " + str(data['dns_queries_today)'] + "\r\n" + "Active Clients: " + str(data['unique_clients']))
		text.UpdateText("time", "time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
		time.sleep(2)
	text.clear() 

