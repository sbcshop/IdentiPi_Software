'''Onboard Display demo code'''
#import required modules 
from IdentiPi import LCD  
from time import sleep
from machine import Pin
import vga1_16x32 as font
import vga1_8x16 as font1
import vga2_8x8 as font2
import vga1_bold_16x32 as fontbold
import st7789


tft = LCD().display() #create instance of display
tft.init()

def msgDisplay():
    tft.text(font,"IdentiPi", 45,30, st7789.YELLOW)
    tft.fill_rect(10, 80, 210,5, st7789.RED)
    tft.text(font1,"SB COMPONENTS", 10,100,st7789.CYAN)
    tft.text(font2,"shop.sb-components.co.uk", 10,120,st7789.WHITE)

msgDisplay()


