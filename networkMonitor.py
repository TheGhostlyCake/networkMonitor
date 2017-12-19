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

from __future__ import print_function
import os, json, urllib3, sys, requests, time
from time import gmtime, strftime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from papirus import Papirus
WHITE = 1
BLACK = 0
TITLE_FONT_FILE = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
BODY_FONT_FILE  = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'

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


# text.Clear()
# text.AddText("NetMan:", 0, 0, Id="start" )
# r = requests.get(url='http://10.0.0.95/admin/api.php')
# data=r.json()
# text.AddText("Ads Block: " + str(data['ads_blocked_today']), 0, 20,15,  Id="ads" )
# text.AddText("DNS queries: " + str(data['dns_queries_today']), 0, 35,15, Id="dns" )
# text.AddText("Active Clients: " + str(data['unique_clients']), 0, 50,15, Id="clients" )
# text.AddText("time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), 0, 65, 12, Id="time" )

def main(argv):
    papirus = Papirus(rotation = int(argv[0]) if len(sys.argv) > 1 else 0)
    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=papirus.panel, w=papirus.width, h=papirus.height, v=papirus.version, g=papirus.cog, f=papirus.film))
    papirus.clear()
    netMan(papirus)

def netMan(papirus):
    """simple partial update demo - draw a clock"""

    # initially set all white background
    image = Image.new('1', papirus.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    width, height = image.size

    title_font_size = 12      # 8 chars HH:MM:SS
    title_font = ImageFont.truetype(TITLE_FONT_FILE, clock_font_size)
    body_font_size = 10     # 10 chars YYYY-MM-DD
    body_font = ImageFont.truetype(BODY_FONT_FILE, body_font_size)

    # clear the display buffer
    draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
    previous_time = 0
	previous_clients =0
	previous_ads=0
	previous_dns=0

    draw.text((10, 10), 'NetMan', fill=BLACK, font=body_font)
    
	while True:
		for x in range(0, 100):
			if previous_ads != int(data['ads_blocked_today'])):
				draw.rectangle((2, 2, width - 2, height - 2), fill=WHITE, outline=BLACK)		
				draw.rectangle((5,10),"Ads Block: " + str(data['ads_blocked_today']), fill=BLACK, font=body_font)
				previous_ads = data['ads_blocked_today'])
			else:
				draw.rectangle((5, 10, width - 5, 10 + clock_font_size), fill=WHITE, outline=WHITE)
			papirus.display(image)
			papirus.partial_update()
			time.sleep(0.5)
		papirus.update()
	
	

	    







    while True:
        while True:
            now = datetime.today()
            if now.second != previous_second:
                break
            time.sleep(0.1)

        if now.day != previous_day:
            draw.rectangle((2, 2, width - 2, height - 2), fill=WHITE, outline=BLACK)
            draw.text((10, clock_font_size + 10), '{y:04d}-{m:02d}-{d:02d}'.format(y=now.year, m=now.month, d=now.day), fill=BLACK, font=date_font)
            previous_day = now.day
        else:
            draw.rectangle((5, 10, width - 5, 10 + clock_font_size), fill=WHITE, outline=WHITE)

        draw.text((5, 10), '{h:02d}:{m:02d}:{s:02d}'.format(h=now.hour, m=now.minute, s=now.second), fill=BLACK, font=clock_font)

        # display image on the panel
        papirus.display(image)
        if now.second < previous_second:
            papirus.update()    # full update every minute
        else:
            papirus.partial_update()
        previous_second = now.second


# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))

    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass