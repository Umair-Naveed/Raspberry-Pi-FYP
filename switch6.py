import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
channel_id = "832459"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "181":
		GPIO.output(18, GPIO.HIGH)
	if state.text == "180":
		GPIO.output(18, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)
