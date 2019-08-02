import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
channel_id = "832514"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "261":
		GPIO.output(26, GPIO.HIGH)
	if state.text == "260":
		GPIO.output(26, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)