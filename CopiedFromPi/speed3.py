import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
channel_id = "832513"
#def main():
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "191":
		GPIO.output(19, GPIO.HIGH)
		#print "LED3 ON"
	if state.text == "190":
		GPIO.output(19, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)