import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
channel_id = "814144"
#def main():
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id
	state = requests.get(baseurl)
	if state.text == "61":
		GPIO.output(6, GPIO.HIGH)
		#print "LED1 ON"
	elif state.text == "60":
		GPIO.output(6, GPIO.LOW)
		#print "LED1 OFF"
	elif state.text == "131":
		GPIO.output(13, GPIO.HIGH)
		#print "LED2 ON"
	elif state.text == "130":
		GPIO.output(13, GPIO.LOW)
		#print "LED2 OFF"
	elif state.text == "191":
		GPIO.output(19, GPIO.HIGH)
		#print "LED3 ON"
	elif state.text == "190":
		GPIO.output(19, GPIO.LOW)
		#print "LED3 OFF"
	elif state.text == "261":
		GPIO.output(26, GPIO.HIGH)
	elif state.text == "260":
		GPIO.output(26, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)