import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
channel_id = "830206"
#def main():
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "221":
		GPIO.output(22, GPIO.HIGH)
		#print "LED3 ON"
	elif state.text == "220":
		GPIO.output(22, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)
