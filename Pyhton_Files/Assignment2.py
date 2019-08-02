import RPi.GPIO as GPIO
import time

def blink(pin):
    GPIO.output(11, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(4)

def main():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(16, GPIO.IN)

    GPIO.output(11, GPIO.HIGH)

    while True:
        if GPIO.input(16):
            blink(11)
        else:
            pass
        time.sleep(.1)

    GPIO.cleanup()

if __name__ == "__main__":
    main()