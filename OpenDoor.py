import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
channel_id = "832464"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "251":
		GPIO.output(25, GPIO.HIGH)
	if state.text == "250":
		GPIO.output(25, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)