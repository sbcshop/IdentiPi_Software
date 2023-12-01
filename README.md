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

- (1) 5-Way Joystick
- (2) 1.14” TFT Display
- (3) Fingerprint sensor
- (4) Fingerprint UART breakout
- (5) Scan Status LED
- (6) Header pin for Pico 
- (7) & (8) Pico GPIOs breakout 

### Interfacing Details

<img src="https://github.com/sbcshop/IdentiPi_Software/blob/main/images/picow_identiPi_interfacing.png" width="478" height="320">
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

With Pico or Pico W connected to IdentiPi, you can proceed to follow below steps to get start working with IdentiPi. 

### 1. How to Install Boot Firmware in Pico W of IdentiPi 

- If you already have MicroPython firmware with the inbuilt ST7789 module, then you can skip this step and jump to **step 2** for trying demo codes.
- In case, you need to add **MicroPython firmware** in Pico of IdentiPi. First, you need to *Press and Hold* the boot button on pico W of IdentiPi, and then, without releasing the button, connect it to PC/laptop using micro USB cable. Check below image for reference,
  
  <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif" width="340" height="228">

- Now your device is in boot mode, and you will see a new mass storage device named "RPI-RP2" as shown in the below figure.
  <img src= "https://github.com/sbcshop/PiCoder-Software/blob/main/images/RPI_folder.jpg" width="720" height="360"/>

- Download the MicroPython firmware file provided in this repo above as ["**_IdentiPi_firmware.uf2_**"](https://github.com/sbcshop/IdentiPi_Software/blob/main/IdentiPi_firmware.uf2). Drag and drop this **_IdentiPi_firmware.uf2_** file onto the RPI-RP2 volume. Your Pico W will reboot. You are now running MicroPython on IdentiPi's pico.
  <img src= "https://github.com/sbcshop/IdentiPi_Software/blob/main/images/fimware_upload.jpg" width="626" height="476">
  
### 2. Running First Program in IdentiPi
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Download this github which contains various examples and open anyone of example in Thonny.

     <img src= "https://github.com/sbcshop/IdentiPi_Software/blob/main/images/identiPi_git_download.jpg" />

   - Now we have **Thonny IDE application** and github example codes, Connect IdentiPi with Pico to laptop/PC. Open any example code in Thonny IDE. Then select micropython device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.

     <img src="https://github.com/sbcshop/IdentiPi_Software/blob/main/images/board_select.jpg">
  
   - Make sure to save _**IdentiPi.py**_ library file to device to avoid any execution error.

      <img src= "https://github.com/sbcshop/IdentiPi_Software/blob/main/images/IdentiPi_library.jpg" />

   - Once everything all set, with any demo code open click on green play button to test program on IdentiPi.

     <img src= "https://github.com/sbcshop/IdentiPi_Software/blob/main/images/run_program.jpg" />

   - For standalone execution without thonny you need to transfer your script into Pico of IdentiPi as main.py, so when again power up board it will start executing saved script. 

     <img src= "https://github.com/sbcshop/IdentiPi_Software/blob/main/images/standalone_execution.jpg" />

     Try out below provided reference example demo codes and modify to build your own application codes.

### How to move any script codes on Pico/Pico W
   - Single File transfer, click on **File -> Save Copy -> select Raspberry Pi Pico** , Then save file as **main.py**
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
   - Move multiple files at one go, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />

### Example Codes
   Try reference demo codes to test onboard components of IdentiPi. Save whatever example code file you want to try as **main.py** in **Pico/Pico W** or Run directly from Thonny IDE by clicking green play button
   - [Display Demo](https://github.com/sbcshop/IdentiPi_Software/blob/main/examples/Demo_LCD.py) : code to test display
   - [Joystick Demo](https://github.com/sbcshop/IdentiPi_Software/blob/main/examples/Demo_Joystick.py) : code to work with onboard joystick
   - [Fingerprint Demo](https://github.com/sbcshop/IdentiPi_Software/blob/main/examples/Demo_Add_Fingerprint.py) : Register fingerprint using onboard fingerprint sensor
   - and [More..](https://github.com/sbcshop/IdentiPi_Software/tree/main/examples)
   
   Using this sample code as a guide, you can modify, build, and share codes!!
   
   We have provided [_**IdentiPi.py**_](https://github.com/sbcshop/IdentiPi_Software/blob/main/examples/IdentiPi.py) library file with most of commands related to fingerprint operations. You can refer [**Fingerprint Command Manual**](https://github.com/sbcshop/IdentiPi_Software/blob/main/documents/Fingerprint_Sensor_Command_Manual.docx.pdf) to understand more commands and particular response from module to modify or update library file as per your applications.
     
   
## Resources
  * [Schematic](https://github.com/sbcshop/IdentiPi_Hardware/blob/main/Design%20Data/Sch%20IdentiPi.pdf)
  * [Hardware Files](https://github.com/sbcshop/IdentiPi_Hardware)
  * [Step File](https://github.com/sbcshop/IdentiPi_Hardware/blob/main/Mechanical%20Data/IdentiPi.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
  * [Fingerprint Command Manual](https://github.com/sbcshop/IdentiPi_Software/blob/main/documents/Fingerprint_Sensor_Command_Manual.docx.pdf)

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
