import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
val = False
while True:
        push_button = GPIO.input(24)
        val = not val or push_button == GPIO.HIGH
        if val:
                print "LED on"
                GPIO.output(18, GPIO.HIGH)
        else:
                print "LED off"
                GPIO.output(18, push_button)
        time.sleep(1)