## EEPROM Pinout and Connection    
![EEPROM Pinout](https://www.instructables.com/files/orig/FTE/IJ63/KLZ5ZQQL/FTEIJ63KLZ5ZQQL.png?auto=webp&frame=1&fit=bounds&md=da8b40e15e23bf41789611a502991127)    
The EEPROM has 8 pins, of which 3 are address pins as shown in the figure. The communication between the EEPROm and the microcontroller is via I2C. By setting the address pins A0, A1, A2 to either high or low, the default I2C address of the EEPROM chip can be configured. It is suggested to connect all the address pins to ground, unless you have multiple I2C devices or multiple EEPROMs connected.   

The WP or Write Protect pin when set to high prevents anything from being written on to the EEPROM. When the WP pin is connected to ground, write protection is disabled and things can be written on to the EEPROM.   

And then there is is the usual SDA (I2C Data), SCL (I2C Clock), Vcc (Supply) and Gnd (Ground) pins.    

The SDA, SCL and WP should not be left floating and hence they need to be pulled up via 3.9k resistors. The schematic for the EEPROM has also been attached. Please go through the same for clarity.   

![EEPROM Schematic](https://www.instructables.com/files/orig/FNH/6HS1/KLZ5ZQWS/FNH6HS1KLZ5ZQWS.png?auto=webp&frame=1&fit=bounds&md=0fe458e58206d807f311a0e2c7566597)     


## EEPROM PCB    
I have designed PCBs for making the Pi Pico-EEPROM connection easier. There are variants to the PCB designed. In the sample PCB image, you can see that one has a jumper for write protection and in the other, the write protection pin has been exposed.    

![EEPROM Board with WP Pin](https://www.instructables.com/files/orig/FR6/WAGD/KLZ5ZQZ3/FR6WAGDKLZ5ZQZ3.png?auto=webp&frame=1&fit=bounds&md=4b38fe77ce233b54199531bbd923523f)     

![EEPROM Board with Jumper](https://www.instructables.com/files/orig/F4Z/VCQK/KLZ5ZQZ4/F4ZVCQKKLZ5ZQZ4.png?auto=webp&frame=1&fit=bounds&md=bb33e26b027c6034d00a73cf04d3dd52)     

The advantage of using the board with the write protection pin exposed is that, the write protection can be software controlled, i.e., it can be enabled or disabled by setting the pin to Low or High.   

Other than the SMD versions, I have designed DIP versions as well. You can find the eagle files and gerber files here in the aobe folders.   

I got myself the SMD version of the board with the write protection pin exposed printed. I used the services of https://jlcpcb.com for printing as like all my projects. Feel free to modify the the board layout, schematics for your project and get them printed or make your own board using a general purpose PCB.   


## EEPROM-Pi Pico Connection    
My connection is as follows:    

EEPROM SDA --> Pi Pico GP0    

EEPROM SDA --> Pi Pico GP1    

EEPROM VCC --> Pi Pico 3V3 (OUT)    

EEPROM WP --> Pi Pico GND    

EEPROm GND --> Pi Pico GND    

The Raspberry Pi Pico has a number of I2C lines. Choose the ones comfortable to you.    


## Using the EEPROM in Your Program   
I have used Micropython to work with the EEPROM chip. I have modified the Micropython EERPOM libraries of [Mike Causer](https://github.com/mcauser).      

There are two parameters of the EEPROM to consider which are the bytes per page(bpp or BPP) and the pages. The total EEPROM memory is BPP x Number of Pages.    

For the same EEPROM capacity different manufactures may have different values of BPP and Number of Pages. Make sure to check them out and change those values in the library files.    

I have provided library files for two different versions just for reference and to show the difference. If you are using any other EEPROM version please do pay attention to the shown differences and change your library file accordingly.    

After making the desired changes to the library file, import it onto the Pi Pico. I have provided a demo script that exploits almost all the functions of the EEPROM. You cna find the demo script in the examples folder.   

I have gone through a lot of detail and have explained the demo script in this video below.    

[![](http://img.youtube.com/vi/LSoozXsghZQ/0.jpg)](http://www.youtube.com/watch?v=LSoozXsghZQ "")    
