
![github-small](https://github.com/shivasiddharth/Raspberry-Pi-Pico/blob/main/Raspberry%20Pi%20Pico%20Pinout.png?raw=true)    


# Raspberry-Pi-Pico
 Aggregate of Raspberry Pi Pico related codes, firmware, libraries, etc.      


*************************************
## Getting started with Micropython    
*************************************   

### Setting the firmware    
1. Download the MicroPython firmware from the **Firmware** directory in the **Micropython** folder or from official Raspberry Pi's site by clicking [here](https://www.raspberrypi.org/documentation/pico/getting-started/static/5d8e777377e8dbe23cf36360d6efc727/pico_micropython_20210121.uf2).     
2. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is detected.     
3. It will mount as a Mass Storage Device called RPI-RP2.     
4. Place the MicroPython UF2 file onto the RPI-RP2 volume. The Raspberry Pi Pico should reboot and ready for programming using Micropython.   

### Programming the Pico   
1. You can use any Micropython based IDE for programming the Pico. However, the recommended IDE is the Thonny.     
2. Raspberry Pi boards come with Thonny preinstalled. If you are using other systems, you can download and install Thonny from [here](https://thonny.org).    
3. To program the Pico, after opening the Thonny IDE, click on **Run** menu and click on the **Select interpreter** option. And from the Drop-down, select Raspberry Pi Pico.    



**************************************
## Getting started with Circuitpython     
**************************************    

### Setting the firmware
1. Download the MicroPython firmware from the **Firmware** directory in the **Circuitpython** folder or from official Adafruit's site by clicking [here](https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-6.2.0-beta.0.uf2).     
2. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is detected.     
3. It will mount as a Mass Storage Device called RPI-RP2.     
4. Place the Circuitpython UF2 file onto the RPI-RP2 volume. The Raspberry Pi Pico should reboot and ready for programming using Micropython.   

### Programming the Pico   
1. You can use any Circuitpython based IDE for programming the Pico. However, the recommended IDE is the Mu.     
2. Raspberry Pi boards come with Thonny preinstalled. If you are using other systems, you can download and install Mu from [here](https://codewith.mu).    
3. To program the Pico, after opening the Mu IDE. Click on the Serial menu to automatically connect your Pico to the Mu IDE.   


## Credits to      
1. Adafruit for the Circuitpython libraries and firmware.  
2. Raspberry Pi Foundation for the firmware.   
