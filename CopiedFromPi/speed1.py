import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
channel_id = "832509"
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "61":
		GPIO.output(6, GPIO.HIGH)
	elif state.text == "60":
		GPIO.output(6, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)