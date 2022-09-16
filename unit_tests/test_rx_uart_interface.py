from tlslite.aux_interface import UartInterface

rx = UartInterface("/dev/ttyAMA0", 9600)
buf = rx.recv_all()
print(buf)