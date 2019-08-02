import RPi.GPIO as GPIO
import httplib, urllib, requests
import string
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
channel_id = "814144"
#def main():
sleep(5)
while True:
	baseurl = ("https://api.thingspeak.com/channels/%s/fields/1/last") % channel_id
	state = requests.get(baseurl)
	if state.text == "171":
		GPIO.output(17, GPIO.HIGH)
		#print "LED1 ON"
	elif state.text == "170":
		GPIO.output(17, GPIO.LOW)
		#print "LED1 OFF"
	elif state.text == "271":
		GPIO.output(27, GPIO.HIGH)
		#print "LED2 ON"
	elif state.text == "270":
		GPIO.output(27, GPIO.LOW)
		#print "LED2 OFF"
	elif state.text == "221":
		GPIO.output(22, GPIO.HIGH)
		#print "LED3 ON"
	elif state.text == "220":
		GPIO.output(22, GPIO.LOW)
		#print "LED3 OFF"
	elif state.text == "161":
		GPIO.output(16, GPIO.HIGH)
	elif state.text == "160":
		GPIO.output(16, GPIO.LOW)
	elif state.text == "201":
		GPIO.output(20, GPIO.HIGH)
	elif state.text == "200":
		GPIO.output(20, GPIO.LOW)
	elif state.text == "181":
		GPIO.output(18, GPIO.HIGH)
	elif state.text == "180":
		GPIO.output(18, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)

#if __name__ == "__main__":
#	main()
#=============================================
