import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
channel_id = "832511"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "131":
		GPIO.output(13, GPIO.HIGH)
	if state.text == "130":
		GPIO.output(13, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)