import serial

from config import serial_port, baudRate

KEY_F1 = '!'
KEY_F2 = '@'
KEY_F3 = '#'
KEY_F4 = '$'
KEY_F5 = '%'
KEY_CTRL_1 = '^'
KEY_CTRL_2 = '&'
KEY_CTRL_3 = '*'
KEY_HUNT = '('

PAUSE_MAGIC = 'magic'
PAUSE_KEY = 'key'

PAUSE_DETECT ='<<'
SUSPEND_DETECT ='>>'

class Connect_serial(object):
    ser = None
    def __init__(self):
        self.ser = serial.Serial(serial_port, baudRate)

    def pushKey(self,_keyCode):
        self.ser.write((_keyCode).encode())

