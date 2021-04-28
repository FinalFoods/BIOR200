#!/usr/bin/env python3
import time
import piplates.DAQC2plate as DAQC2
import RPi.GPIO as GPIO

def int_handler(int_num):
	mask = DAQC2.getINTflags(0)
	print("interrupt from ", int_num, "mask ", hex(mask))

if __name__ == '__main__':
        GPIO.setmode(GPIO.BCM)
        pin = 0
        DAQC_GPIO = 22 

        GPIO.setup(DAQC_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(DAQC_GPIO, GPIO.FALLING, callback=int_handler, bouncetime=300)
 
        DAQC2.intEnable(0)
        DAQC2.enableDINint(0, pin, 'b')
        print("enabled edge interrupt for pin ", pin)

        while True:
                time.sleep(0.2)
                din = DAQC2.getDINbit(0, pin)
                print("digital input pin:", pin, "value:", din)
                print(DAQC_GPIO, GPIO.input(DAQC_GPIO))

