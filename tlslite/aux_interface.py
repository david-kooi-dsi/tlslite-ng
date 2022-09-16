import time
import serial

SERIAL_READ_TIMEOUT_S = 1

class AuxiliaryInterface():
    """
    An interface that allows bytes to be sent and recieved 
    over an alternative medium. 
    """
    def send(self, data: bytearray):   
        raise NotImplementedError
    
    def recv_all(self):
        raise NotImplementedError

class UartInterface(AuxiliaryInterface):
    def __init__(self, port: str, baud: int):
        self._ser = serial.Serial(
            port = port,
            baudrate=baud,
            timeout=SERIAL_READ_TIMEOUT_S
        )

    def send(self, data)-> int:
        print(f"UartInterface Sending: {len(data)} bytes")
        self._ser.write(data)
        self._ser.flush()
        return len(data)
    
    def recv_all(self, timeout_s=10) -> bytearray:
        buf = bytearray(0)
        
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout_s:
                print("UartInterface Recv timeout.")
                break
            if bool(self._ser.in_waiting):
                byte = self._ser.read()
                if byte != b'\n':
                    buf += byte
                else:
                    break
        print(f"UartInterface received {len(buf)} bytes")
        return buf