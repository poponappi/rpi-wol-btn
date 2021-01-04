# Raspberry Pi WOL Button
Button connected to Raspberry Pi's gpio port send Wake-On-Lan signal to computer to start it.

## About project

I made this so I can hide my computer out of sight. Thats why I can't reach power button of computer.


## Requirements

### Software Requirements
Python 3
GPIOzero - Raspberry Pi GPIO module for python
wakeonlan - A small python module for wake on lan.

### Hardware Requirements

Raspberry Pi - Tested on RPI Zero W, but should work on any Raspberry pi
Button
wires
soldering iron
some tin

## Hardware installation

Solder one wire to gpio port 2 and the other side to button's connector. Second wire need to bee solderred to Ground(GPIO14) and the other end of that goes to buttons other connector.

