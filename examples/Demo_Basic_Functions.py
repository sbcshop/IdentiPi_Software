'''
Demo code to perform some basic operations using fingerprint sensor, for more operations
Refer Command Manual:
https://github.com/sbcshop/IdentiPi_Software/blob/main/documents/Fingerprint_Sensor_Command_Manual.docx.pdf

'''
from machine import Pin
from IdentiPi import FP
import time
import os

enable_pin = Pin(3,Pin.OUT)
enable_pin.value(0) # (0)Enable the Module,(1)Disable the Module

fp = FP()	#create instance 

#Uncomment corresponding functions to test and comment others

'''
Count all users from the device
'''
print(fp.user_count())

'''
Sleep the module
'''
#fp.Sleep()


'''
Delete user from the device, provide corresponding p1 & p2 value from ID to delete
'''
#fp.Delete_user(78,45)


'''
Wake up module from sleep
'''
#fp.Wake_up()


'''
CAUTION: Using this command will DELETE ALL USERS FINGERPRINT from the device
'''
#fp.Delete_all_users()
