# Frangitron Photobooth

Rewrite of the Raspberry Pi Photobooth

# Installation

## Operating system

- Use HDMI display (unplug touchscreen)
- Install Manjaro (ARM Raspberry XFCE, guide written with 23.02)
  - create default user `photobooth` 
- Update whole system with `sudo pacman -Syu`
- Edit `/boot/config.txt`
````
console=tty1
display_auto_detect=1
````
- Add to `/boot/cmdline.txt`
````
 fbcon=rotate:2
````
- Shutdown
- Plug touchscreen, unplug HDMI
- Boot
- Rotate display using GUI `All Applications > Display`
- Edit `/usr/share/X11/xorg.conf.d/40-libinput.conf` by adding to section `touchscreen`
````
Option "TransformationMatrix" "-1 0 1 0 -1 1 0 0 1"
````
- Disable screensaver and lock screen using GUI `All Applications > Screensaver`
- Disable screen blanking using GUI `All Applications > Power Manager`

## GPIO access

- Create group and add user

````
sudo groupadd gpio
sudo usermod -a -G gpio photobooth
````

- Create rules files `/etc/udev/rules.d/90-gpio.rules` with content

````
KERNEL=="gpiomem", OWNER="root", GROUP="gpio"
````

## Python environment

- Install

````
sudo pacman -Syu pyside6
sudo pacman -Syu qt6
sudo pacman -Syu python-pip
sudo pacman -Syu python-virtualenv
````

- Create virtualenv (in `~/`)

````
virtualenv --system-site-packages ~/photobooth-venv
~/photobooth-venv/bin/python3 -m pip install --upgrade pip
````

- Install Photobooth

````
~/photobooth-venv/bin/pip install git+https://github.com/MrFrangipane/frangitron_photobooth.git
````
