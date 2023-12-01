'''
Demo to register new fingerprint

'''
#import required module 
from machine import Pin
from IdentiPi import FP		
import time
import os

enable_pin = Pin(3,Pin.OUT)
enable_pin.value(0) # (0)Enable the Module,(1)Disable the Module

fp = FP()	#create instance of fingerprint

'''
Need Hexadecimal value of ID's as shown below:
p1, p2, p3 => 2F A3 45

p3 - must be Non-zero value
'''
p1,p2,p3 = input("User ID p1,p2,p3 = ").split()
time.sleep(2)

'''
For proper detection fingerprint scan for 3 times
'''
# Make sure not change the for loop counting , loop must be 3 times
def add_finger():
    for i in range(1,4):
        r = fp.add_fingerprint(p1,p2,p3,str(i)) # 0.2 - time
        time.sleep(0.5)
        if r is not None:
            print(r)
                  
add_finger()