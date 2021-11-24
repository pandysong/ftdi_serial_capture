from argparse import ArgumentParser
import signal

# Enable pyserial extensions
import pyftdi.serialext

argparser = ArgumentParser()

default_device = "ftdi:///3"
argparser.add_argument('device', nargs='?', default=default_device,
                       help='serial port device name (default: %s)' %
                       default_device)
argparser.add_argument('-b', '--baudrate',
                       help='serial port baudrate (default: 6000000)',
                       default=6000000)
argparser.add_argument('-f', '--file',
                       help='save dump to a file',
                       default='capture.bin')

args = argparser.parse_args()

# Open a serial port on the second FTDI device interface
port = pyftdi.serialext.serial_for_url(args.device, args.baudrate)

# Receive bytes

cnt = 0
with open(args.file, 'wb') as f:
    stop = False
    while not stop:
        try:
            data = port.read(1024)
            cnt = cnt + len(data)
            f.write(data)
            print("\rcapture size: {}".format(cnt), end="")
        except KeyboardInterrupt:
            stop = True
