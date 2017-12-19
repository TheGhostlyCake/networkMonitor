# Copyright 2013-2015 Pervasive Displays, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#   http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.  See the License for the specific language
# governing permissions and limitations under the License.
 

 # License above available from papirus library: https://github.com/PiSupply/PaPiRus

from papirus import PapirusTextPos
import os, json, urllib3
import requests
import time
from time import gmtime, strftime
text = PapirusTextPos(rotation=0)
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

WHITE = 1
BLACK = 0

CLOCK_FONT_FILE = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
DATE_FONT_FILE  = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'









# Check EPD_SIZE is defined
EPD_SIZE=0.0
if os.path.exists('/etc/default/epd-fuse'):
    exec(open('/etc/default/epd-fuse').read())
if EPD_SIZE == 0.0:
    print("Please select your screen size by running 'papirus-config'.")
    sys.exit()

# Running as root only needed for older Raspbians without /dev/gpiomem
if not (os.path.exists('/dev/gpiomem') and os.access('/dev/gpiomem', os.R_OK | os.W_OK)):
    user = os.getuid()
    if user != 0:
        print("Please run script as root")
        sys.exit()


text.Clear()
text.AddText("NetMan:", 0, 0, Id="start" )
r = requests.get(url='http://10.0.0.95/admin/api.php')
data=r.json()
text.AddText("Ads Block: " + str(data['ads_blocked_today']), 0, 20,15,  Id="ads" )
text.AddText("DNS queries: " + str(data['dns_queries_today']), 0, 35,15, Id="dns" )
text.AddText("Active Clients: " + str(data['unique_clients']), 0, 50,15, Id="clients" )
text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

def main(argv):
    papirus = Papirus(rotation = int(argv[0]) if len(sys.argv) > 1 else 0)
    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=papirus.panel, w=papirus.width, h=papirus.height, v=papirus.version, g=papirus.cog, f=papirus.film))
    papirus.clear()
    demo(papirus)

def netMan(papirus):
    """simple partial update demo - draw a clock"""

    # initially set all white background
    image = Image.new('1', papirus.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    width, height = image.size

    clock_font_size = int((width - 4)/(8*0.65))      # 8 chars HH:MM:SS
    clock_font = ImageFont.truetype(CLOCK_FONT_FILE, clock_font_size)
    date_font_size = int((width - 10)/(10*0.65))     # 10 chars YYYY-MM-DD
    date_font = ImageFont.truetype(DATE_FONT_FILE, date_font_size)

    # clear the display buffer
    draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
    previous_second = 0
    previous_day = 0

    while True:
        
        if now.day != previous_day:
            draw.rectangle((2, 2, width - 2, height - 2), fill=WHITE, outline=BLACK)
            draw.text((10, clock_font_size + 10), 'hi', fill=BLACK, font=date_font)
            previous_day = now.day
        else:
            draw.rectangle((5, 10, width - 5, 10 + clock_font_size), fill=WHITE, outline=WHITE)

        draw.text((5, 10), 'there', fill=BLACK, font=clock_font)

        # display image on the panel
        papirus.display(image)
        if now.second < previous_second:
            papirus.update()    # full update every minute
        else:
            papirus.partial_update()
        previous_second = now.second





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
	
