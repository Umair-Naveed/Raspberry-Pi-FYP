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
channel_id1 = "814144"
channel_id2 = "830195"
channel_id3 = "830206"
channel_id4 = "830217"
#def main():
sleep(5)
while True:
	baseurl1 = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id1
	baseurl2 = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id2
	baseurl3 = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id3
	baseurl4 = ("https://api.thingspeak.com/channels/%s/fields/1/last" )% channel_id4
	state1 = requests.get(baseurl1)
	state2 = requests.get(baseurl2)
	state3 = requests.get(baseurl3)
	state4 = requests.get(baseurl4)
	if state1.text == "171":
		GPIO.output(17, GPIO.HIGH)
		#print "LED1 ON"
	elif state1.text == "170":
		GPIO.output(17, GPIO.LOW)
		#print "LED1 OFF"
	elif state2.text == "271":
		GPIO.output(27, GPIO.HIGH)
		#print "LED2 ON"
	elif state2.text == "270":
		GPIO.output(27, GPIO.LOW)
		#print "LED2 OFF"
	elif state3.text == "221":
		GPIO.output(22, GPIO.HIGH)
		#print "LED3 ON"
	elif state3.text == "220":
		GPIO.output(22, GPIO.LOW)
		#print "LED3 OFF"
	elif state4.text == "161":
		GPIO.output(16, GPIO.HIGH)
	elif state4.text == "160":
		GPIO.output(16, GPIO.LOW)
	else:
		print "NOT Command"
		sleep(1)

#if __name__ == "__main__":
#	main()
#=============================================
