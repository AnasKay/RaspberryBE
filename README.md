# RaspberryBE
Code is written for Raspberry PI 4
in order to use it you should enable the second UART on your raspi 
I added in the /boot/config.txt  the following:
dtoverlay=uart4
and executed afterwards
sudo dtoverlay uart4
executing "raspi-gpio get 0-15" will show you which pins are rx/tx
