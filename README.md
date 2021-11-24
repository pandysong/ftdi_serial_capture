# Dump Data from FTDI Serial Port to Binary File on MacOS

This is a simple tool to capture the data from FTDI devices to a binary file.


# Why Another tool

In Mac OSX, FTDI device could only work up to 4M baud rate, it is not possible
to run 6M baud rate which I need.

# Dependency

## FTDI D2XX Driver

This is the driver to replace the standard VCP (Virtual Com Port Driver).

Following the video to install the driver on Mac

```
https://www.youtube.com/watch?v=Ir2PVz1870E
```

Find the driver:

```
https://ftdichip.com/wp-content/uploads/2021/05/D2XX1.4.24.zip
```

On following page:

```
https://ftdichip.com/drivers/d2xx-drivers/
```

## pyftdi

Refer to the following document to install pyftdi:

```
https://eblot.github.io/pyftdi/
```

# How to use

```
ftdi_dump(master ✗) python3 dump.py -h
usage: dump.py [-h] [-b BAUDRATE] [-f FILE] [device]

positional arguments:
  device                serial port device name (default: ftdi:///3)

optional arguments:
  -h, --help            show this help message and exit
  -b BAUDRATE, --baudrate BAUDRATE
                        serial port baudrate (default: 6000000)
  -f FILE, --file FILE  save dump to a file
```
