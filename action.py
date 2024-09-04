
import pyautogui

from connect.con_serial import KEY_F1, KEY_F2, KEY_HUNT


def actionHealth(serial_connect,healthWrap):
    # if healthWrap.type == 'hp':
    key = KEY_F1 if healthWrap.type == 'hp' else KEY_F2
    serial_connect.pushKey(key)

def actionHunt(serial_connect):
    serial_connect.pushKey(KEY_HUNT)

def actionMoveForTarget(serial_connect,x_position,y_position):
        current_x, current_y = pyautogui.position()
        x_move = x_position - current_x
        y_move = y_position - current_y
        print(f'마우스 이동 {x_move} {y_move}')
        serial_connect.pushKey(f'~{x_move} {y_move}')

def actionBuff(serial_connect):
    print('actionBuff')

def actionmagic(serial_connect):
    print('actionmagic')


def calcDefaultPosition(wrap):

    return
