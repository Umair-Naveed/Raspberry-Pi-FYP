import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
channel_id = "830195"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "271":
		GPIO.output(27, GPIO.HIGH)
		#print "LED2 ON"
	elif state2.text == "270":
		GPIO.output(27, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)