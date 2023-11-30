# IdentiPi_Software

<img src="https://github.com/sbcshop/IdentiPi_Software/blob/main/images/IdentiPi_banner.jpg">

Fingerprint HAT for Raspberry Pi Pico - an innovative solution for secure biometric authentication. This HAT is an ideal tool for developing unique projects, Experience rapid and stable fingerprint verification with our Fingerprint HAT.

An in-depth setup and working guide for IdentiPi is available on this github. 

### Features:
- Onboard Fingerprint Sensor module
- HAT compatible with Raspberry Pico/Pico W 
- Status LED for Fingerprint scan indication.
- Fingerprint sensor Serial TX/RX pin breakout 
- 1.14” Display for visual interaction in your project
- 5-Way Joystick for adding additional control features in project


### Specifications:
- Microcontroller Support: Raspberry Pi Pico / Pico W
- Board Supply voltage: 5V
- Board Operating Voltage: 3.3V
- Display:
 	* Display Size: 1.14"
 	* Display Type: TFT
 	* Display Resolution:  135(H) X 240(V) pixels
 	* Display colors: 65K/262K RGB
 	* Luminance(cd/m2): 400(TYP)
 	* Display interface: SPI
 	* Display Driver: ST7789V
- Fingerprint Sensor:
  * Sensor type: capacitive touching
  * Resolution: 508DPI
  * Image pixels: 192×192
  * Image grey scale: 8
  * Sensor size: R15.5mm
  * Fingerprint capacity: 500
  * Matching time: <500ms (1:N, and N≤100)
  * Interface: UART
  * Baudrate: 19200 bps
  * Life: 1 million times
- Operating environment:
 	* Temperature: -20°C~70°C
 	* Humidity: 40%RH~85%RH (no condensation)
- Storage environment:
 	* Temperature: -40°C~85°C
 	* Humidity: <85%RH (no condensation)


## Getting Started with IdentiPi
### Hardware Overview
#### Pinout

<img src="https://github.com/sbcshop/IdentiPi_Software/blob/main/images/IdentiPi_pinout.jpg">

- 1) 5-Way Joystick
- 2) 1.14” TFT Display
- 3) Fingerprint sensor
- 4) Fingerprint UART breakout
- 5) Scan Status LED
- 6) Header pin for Pico 
- 7) &  8) Pico GPIOs breakout 

### Interfacing Details

<img src="">
When Raspberry Pico W connected with HAT following pins consumed,  

- Fingerprint Module interfacing info
  | Pico | Fingerprint Sensor | Function |
  |---|---|---|
  |GP0 (UART0 TX) | F_RX | UART communicatoin pin |
  |GP1 (UART0 RX) | F_TX | UART communicatoin pin |
  |GP3 | P_EN | Fingerprint Enable pin => 0 to Enable and 1 to Disable | 

- Display interfacing details
  | Pico | Hardware Pin | Function |
  |---|---|---|
  |GP10 | SCLK | Clock pin of SPI interface for display |
  |GP11 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP8 | D/C | Data/command line of SPI interface for display |
  |GP12 | RESET | Display reset pin |
  |GP9 | CS   | Chip Select pin of SPI interface for display| 
  |GP13 | BL | Backlight pin for display |

- Joystick interfacing details
  | Pico W | Joystick | Function |
  |---|---|---|
  |GP14 | JY_U |Programmable Joystick button|
  |GP15 | JY_R |Programmable Joystick button|
  |GP16 | JY_L |Programmable Joystick button|
  |GP17 | JY_D |Programmable Joystick button|
  |GP18 | JY_Sel |Programmable Joystick button|
  
 
- Breakout GPIOs
  
<!-- 
### 1. Step to install boot Firmware
   - Every IdentiPi board will be provided with boot firmware already installed, so you can skip this step and directly go to [step 2](https://github.com/sbcshop/PiBeam_Software#2-onboard-led-blink).
   - If in case you want to install firmware for your PiBeam, Push and hold the BOOT button and plug your PiBeam into the USB port of your computer. Release the BOOT button after your PiBeam is connected to USB port.
   - It will mount as a Mass Storage Device called RPI-RP2.
   - Drag and drop the MicroPython UF2 - [PiBeam_firmware](https://github.com/sbcshop/PiBeam_Software/blob/main/PiBeam_firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your PiBeam will reboot. You are now running MicroPython on PiBeam.
   - If you want to use PiBeam as HID then you will have to install other boot firmware, instruction provided on [link](https://github.com/sbcshop/PiBeam_Software/edit/main/examples/HID_example_circuitpython/) 

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect PiBeam to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/onboardLED_demo.py), then click on the green run button to make your script run on PiBeam. Make sure that you have also saved [PiBeam Library](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/PiBeam.py) file to device to avoid any execution error.
     
      <img src= "https://github.com/sbcshop/PiBeam_Software/blob/main/images/LED_blink.png" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug PiBeam, it will stop running. To run your script without using an IDE, simply power up PiBeam and it should run your script, go to step 3.

### 3. How to move your script on PiBeam
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as **main.py**
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico of PiBeam. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/PiBeam_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   - Here, we need only one library file [PiBeam.py](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/PiBeam.py) for most of our code to try out, so move this to PiBeam with default name

   
-->

### Example Codes
   Save whatever example code file you want to try as **main.py** in **Pico/Pico W** or Run directly from Thonny IDE by clicking green play button
   In [example](https://github.com/sbcshop/PiBeam_Software/tree/main/examples) folder you will find demo example script code to test onboard components of IdentiPi like 
   - [Display Demo](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/button_demo.py) : code to test display
   - [Joystick Demo](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/sdcard_demo.py) : code to work with onboard joystick
   - [Fingerprint Demo](https://github.com/sbcshop/PiBeam_Software/blob/main/examples/transmitter_demo.py) : Register fingerprint using onboard fingerprint sensor 
   - 
   
   Using this sample code as a guide, you can modify, build, and share codes!!  


## Resources
  * [Schematic](https://github.com/sbcshop/IdentiPi_Hardware/blob/main/Design%20Data/Sch%20IdentiPi.pdf)
  * [Hardware Files](https://github.com/sbcshop/IdentiPi_Hardware)
  * [Step File](https://github.com/sbcshop/IdentiPi_Hardware/blob/main/Mechanical%20Data/IdentiPi.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
  * [Fingerprint Command Manual](https://github.com/sbcshop/IdentiPi_Software/blob/main/documents/Fingerprint%20Sensor%20Command%20Manual.docx.pdf)

## Related Products
  * [USB Fingerprint](https://shop.sb-components.co.uk/products/usb-fingerprint?_pos=1&_sid=1a14e781e&_ss=r) 

 ![USB Fingerprint](https://shop.sb-components.co.uk/cdn/shop/products/usbfingerprintboard.png?v=1627629405&width=300)
 
 * [PiFinger | Fingerprint HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/pifinger-fingerprint-hat-for-raspberry-pi?_pos=1&_sid=1b596a7b4&_ss=r)
 
 ![PiFinger](https://shop.sb-components.co.uk/cdn/shop/products/FingerprintforRaspberryPi.png?v=1615200690&width=300)
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
