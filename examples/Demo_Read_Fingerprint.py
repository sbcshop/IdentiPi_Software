'''
Demo to code to verify if user exists,
Yes - returns ID
No - message

'''
#import required modules
from machine import Pin
from IdentiPi import FP
import time
import os

enable_pin = Pin(3,Pin.OUT)
enable_pin.value(0) # (0)Enable the Module,(1)Disable the Module

fp = FP() #create instance

print("Count  = ",fp.user_count())	#count no. of fingerprint registered

while 1:
    fp.Read_1_N()		#check for fingerprint present or not
    time.sleep(0.2)
                  