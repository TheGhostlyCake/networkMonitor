from papirus import PapirusTextPos
import os
hostname1="192.168.0.1"
hostname2="192.168.1.254"
hostname3="192.168.0.1"
hostname4="8.8.8.8"












# Same as calling "PapirusTextPos(True [,rotation = rot])"
text = PapirusTextPos(rotation=90)

# Write text to the screen at selected point, with an Id
# "hello world" will appear on the screen at (10, 10), font size 20, straight away
text.AddText("hello world", 10, 10, Id="Start" )

# Add another line of text, at the default location
# "Another line" will appear on screen at (0, 0), font size 20, straight away
text.AddText("Another line", Id="Top")

# Update the first line
# "hello world" will disappear and "New Text" will be displayed straight away
text.UpdateText("Start", "New Text")

# Remove The second line of text
# "Another line" will be removed from the screen straight away
text.RemoveText("Top")

# Clear all text from the screen
# This does a full update so is a little slower than just removing the text.
text.Clear()


def connectiontype:
	response1 = os.system("ping -c 1 " +hostname1)
	response2 = os.system("ping -c 1 " +hostname2)
	response3 = os.system("ping -c 1 " +hostname3)
	response4 = os.system("ping -c 1 " +hostname4)

	if response1 == 0:
		print hostname, 'PiZero down!'
		text.write("PiZero WiFi Down!")
	else if response1 != 0 && response:
		print hostname, "WifiUp"
	
