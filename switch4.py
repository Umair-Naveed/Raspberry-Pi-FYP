import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
channel_id = "830217"
#def main():
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "161":
		GPIO.output(16, GPIO.HIGH)
	elif state.text == "160":
		GPIO.output(16, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)