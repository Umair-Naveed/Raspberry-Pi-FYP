import sys
import Adafruit_DHT
def main():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print (temperature, humidity)
    # temperature = temperature * 9/5.0 + 32
main()