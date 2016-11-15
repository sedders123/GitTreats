import os
from pubnub import Pubnub
import RPi.GPIO as GPIO
import time

pubnub = Pubnub(
    publish_key=os.environ["PUBNUB_GT_PUBLISH"],
    subscribe_key=os.environ["PUBNUB_GT_SUBSCRIBE"])

CHANNEL = "GitTreats"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorForwards = 10

GPIO.setup(pinMotorForwards, GPIO.OUT)

def turn_motor(duration):
    GPIO.output(pinMotorForwards, 1)
    time.sleep(duration)
    GPIO.output(pinMotorAForwards, 0)

def callback(message, channel):
    if message == "Give \'em a treat":
        turn_motor(3)

def main():
    pubnub.subscribe(channels=CHANNEL, callback=callback)

if __name__ == '__main__':
    main()
