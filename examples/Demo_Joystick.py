'''Onboard Joystick demo code'''
#import required modules 
from IdentiPi import LCD
from machine import Pin
from time import sleep
import vga1_16x32 as font
import vga1_8x16 as font1
import vga2_8x8 as font2
import vga1_bold_16x32 as fontbold
import st7789

joyRight = Pin(15,Pin.IN, Pin.PULL_UP)
joyLeft  = Pin(16,Pin.IN, Pin.PULL_UP)
joyUp   = Pin(14,Pin.IN, Pin.PULL_UP)
joyDown  = Pin(17,Pin.IN, Pin.PULL_UP)  
joySel    = Pin(18,Pin.IN, Pin.PULL_UP)

tft = LCD().display()
tft.init()


tft.text(font,"5-Way Joystick", 10,30,st7789.YELLOW)
tft.text(font,"Demo", 80,70,st7789.YELLOW)
sleep(1)

tft.fill(0)
tft.text(font,"Move Joystick!", 10,30,st7789.YELLOW)
sleep(2)

while 1:
    #get current value of buttons, 0 - when pressed and 1 - when released 
    val1 = joyUp.value()
    val2 = joyDown.value()
    val3 = joyLeft.value()
    val4 = joyRight.value()
    val5 = joySel.value()

    if val1 == 0:
        print("JY-RIGHT")
        tft.text(font,"JY-RIGHT", 50,50,st7789.YELLOW)
    elif val2 == 0:
        print("JY-DOWN")
        tft.text(font,"JY-DOWN", 50,50,st7789.YELLOW)
    elif val3 == 0:
        print("JY-LEFT")
        tft.text(font,"JY-LEFT", 50,50,st7789.YELLOW)
    elif val4 == 0:
        print("JY-UP")
        tft.text(font,"JY-UP", 60,50,st7789.YELLOW)
    elif val5 == 0:
        print("JY-Centre")
        tft.text(font,"JY-Centre", 50,50,st7789.YELLOW)
    else :
        tft.fill(0)
        
    sleep(0.2)


