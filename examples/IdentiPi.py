'''
Library Module for IdentiPi 

Add this module into Pico/Pico W to try any examples:
https://github.com/sbcshop/IdentiPi_Software/tree/main/examples

Refer Manual to More commands:
https://github.com/sbcshop/IdentiPi_Software/blob/main/documents/Fingerprint_Sensor_Command_Manual.docx.pdf

'''
#import required libraries 
import machine
from machine import Pin, SPI
import time
import binascii
import array
import os
import st7789

s = []

# Basic response message definition
ACK_SUCCESS           = 0x00
ACK_FAIL              = 0x01
ACK_FULL              = 0x04
ACK_NO_USER           = 0x05
ACK_TIMEOUT           = 0x08
ACK_GO_OUT            = 0x0F
###################################

CMD_HEAD      = "F5"
CMD_TAIL      = "F5"

class LCD:
    def __init__(self):
      self.spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
      
    def display(self):
      self.tft = st7789.ST7789(self.spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)
      return self.tft
        
        
class FP():
    def __init__(self):
        self.serial = machine.UART(0, baudrate=19200, bits=8, parity=None, stop=1, tx=machine.Pin(0), rx=machine.Pin(1))
        self.serial.init(baudrate=19200, bits=8, parity=None, stop=1)
        time.sleep(0.2)
        self.temp = 0
    
    '''
    Calculate checksum
    '''
    def calculate_checksum(self,data):
        checksum = 0
        for byte in data:
            checksum ^= byte
        return checksum

    def calculation(self,Data):
        bin_data1 = binascii.unhexlify(Data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        chk = str(chk_1[2:])
        if len(chk) > 1:
            return chk
        else:
            return '0'+ chk
    
    
    '''
    Put device in sleep mode, disable the module from sleep mode kindly send pulse to module
    '''
    def Sleep(self): 
            fig = '2C'+'00'+'00'+'00'+'00'
            dat = self.calculation(fig)
            dat1 = CMD_HEAD+fig+dat+CMD_TAIL
            data = self.send_command(dat1)
            time.sleep(0.2)
            rec_data = self.serial.read(16)
            s = []
            if rec_data is not None:
                   a = ['{:02x}'.format(x) for x in rec_data]
                   print(a)
                   #self.acknowledge(a[4]) #Acknowledgement
                   
    def Wake_up(self):
        enable_pin = Pin(3,Pin.OUT)
        enable_pin.value(1) # (0)Enable the Module,(1)Disable the Module
        time.sleep(0.2)
        enable_pin.value(0) # (0)Enable the Module,(1)Disable the Module
        time.sleep(0.2)
        
                   

    '''
    There are two mode: enable duplication mode and disable duplication mode. When module is in
    disabled duplication mod: same fingerprint could only added as one ID. If you want to add
    another ID with the same fingerprint, DSP response failed information. Module is in disabled
    mode after powering on.
    
    X1 = 0 : Enable  ,  1: Disable
    X2 = 0 : New mode,  1: Read current mode
    '''
    def Mode(self,X1,X2): 
            lst =['2D','00',X1,X2,'00']
            fig = "".join(lst)
            dat = self.calculation(fig)
            dat1 = CMD_HEAD+fig+dat+CMD_TAIL
            data = self.send_command(dat1)
            time.sleep(0.2)
            rec_data = self.serial.read(16) 
            s = []
            if rec_data is not None:
                   a = ['{:02x}'.format(x) for x in rec_data]
                   self.acknowledge(a[4]) #Acknowledgement
    '''
    Count all users   
    '''
    def user_count(self):
        fig = '09'+'00'+'00'+'00'+'00'
        dat = self.calculation(fig)
        dat1 = CMD_HEAD+fig+dat+CMD_TAIL
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(16)
        s = []
        if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                return a[3] #+a[4]

    '''
    Add fingerprint  
    '''
    def add_fingerprint(self,p1,p2,p3,j):
            P1 = str(p1)
            P2 = str(p2)
            P3 = str(p3)
                
            if self.temp == 0:
                with open('textdata.txt', 'a') as f:
                    f.write('\n')
                    f.write('P1 = ')
                    f.write(P1)
                    f.write('\n')
                    f.write('P2 = ')
                    f.write(P2)
                    f.write('\n')
                    f.write('P3 = ')
                    f.write(P3)
                    f.write('\n')
                    self.temp +=1
            
            lst =['0',P1,P2,P3,'00']
            lst.insert(1,str(j))
            fig = "".join(lst)
            dat = self.calculation(fig)    
            dat1 = CMD_HEAD+fig+dat+CMD_TAIL
            del lst[1]
            data = self.send_command(dat1)
            time.sleep(0.2)
            rec_data = self.serial.read(16) 
            s = []
            if rec_data is not None:
                   a = ['{:02x}'.format(x) for x in rec_data]
                   return self.acknowledge(a[4]) #Acknowledgement
  
    '''
    Delete all users fingerprint from module
    '''
    def Delete_user(self,p1,p2):
        cal_d = '04'+str(p1)+str(p2)+'00'+'00'
        dat = self.calculation(cal_d)
        dat1 = CMD_HEAD+cal_d+ dat+CMD_TAIL
        print(dat1)
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(16) 
        s = []
        if rec_data is not None:
               a = ['{:02x}'.format(x) for x in rec_data]
               self.acknowledge(a[4]) #Acknowledgement
               
    '''
    Delete all users fingerprint from module
    '''
    def Delete_all_users(self):
        cal_d = '05'+'00'+'00'+'00'+'00'
        dat = self.calculation(cal_d)
        dat1 = CMD_HEAD+cal_d+ dat+CMD_TAIL
        print(dat1)
        data = self.send_command(dat1)
        time.sleep(0.2)
        rec_data = self.serial.read(16) 
        s = []
        if rec_data is not None:
               a = ['{:02x}'.format(x) for x in rec_data]
               self.acknowledge(a[4]) #Acknowledgement
               
    '''
    Read finger print 1 to N numbers of people
    '''
    def Read_1_N(self): # read 1:N
        Data = "0C"
        dat = self.calculation(Data)
        dat = CMD_HEAD+Data +'00000000'+dat+CMD_TAIL
        data = self.send_command(dat)
        time.sleep(0.2)
        rec_data = self.serial.read(16) 
        s = []
        if rec_data is not None:
               a = ['{:02x}'.format(x) for x in rec_data]
               if a[2] != '00' and a[3] != '00' and a[4] != '05':
                   print("P1,P2,P3 =  {},{},{}".format(a[2],a[3],a[4]))
                   self.acknowledge(a[4]) #Acknowledgement
               self.acknowledge(a[4]) #Acknowledgement
 
    def send_command(self, data):
        bin_data = binascii.unhexlify(data)
        response = self.serial.write(bin_data)

    def acknowledge(self,ack):
        if ack == '00':
            print("Success")
                
        elif ack == "01":
            print("Failed")
            
        elif ack == "04":
            print("The database is full")
            
        elif ack == "05":
            print("The user is not exist")
                  
        elif ack == "06":
            print("The user was exist")
                   
        elif ack == "07":
            print("The fingerprint was exist")
            
        elif ack == "08":
            print("Time out!")

 



