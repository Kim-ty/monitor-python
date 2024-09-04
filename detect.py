import time

import numpy as np
import win32gui
import win32ui
from PIL import ImageGrab
from PIL import Image

attack_icon = 0
select_icon = 0

def detectHealth(healthWrap):

    healthType = healthWrap.type
    healthGage = np.array(ImageGrab.grab((healthWrap.x_position, healthWrap.y_position,healthWrap.end_x_position, healthWrap.end_y_position)))
    colorPosition = 0 if healthType == 'hp' else 2

    healthState = 0

    for yposition in healthGage[4]:
        if yposition[colorPosition] > 140:
            healthState += 1

    healthPer = int('%.f' % (healthState/len(healthGage[4]) * 100.0))
    return healthPer

def detectBuff(imgName,buffWrap):
    print(imgName + '버프 찾기')
    return 1

class DetectHunt():
    def do_detectHunt(self,cursor_info):
        info = win32gui.GetCursorInfo()
        if cursor_info.attack_cursor is not None:
            if cursor_info.attack_cursor == info[1]:
                return True
            elif cursor_info.select_cursor == info[1]:
                return False
            else :
                cursor_info.attack_cursor = None
                cursor_info.select_cursor = None
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 35, 35)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)

        hdc.DrawIcon((0, 0), info[1])

        target = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)

        # 추출이미지 rgb로 전환
        im = Image.frombuffer(
            'RGB',
            (target['bmWidth'], target['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        # attack 이미지 받아오기

        cursor_img = np.array(im)
        select = np.array_equal(cursor_img,cursor_info.select_np)
        attack = np.array_equal(cursor_img,cursor_info.attack_np)
        if attack:
            cursor_info.attack_cursor = info[1]
        if select:
            cursor_info.select_cursor = info[1]

        # win32gui.DestroyIcon(info[1])
        win32gui.DeleteObject(hbmp.GetHandle())
        hdc.DeleteDC()

        return attack