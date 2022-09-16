from tlslite.aux_interface import UartInterface

rx = UartInterface("/dev/ttyAMA0", 9600)
rx.send(b'Hello World')