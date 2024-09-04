import time
from random import randint

import pyautogui

from action import actionHealth, actionHunt, actionMoveForTarget
from detect import detectBuff, detectHealth, DetectHunt
from m_cursor import M_cursor


class MonitorThreading():
    isStarted = False
    serial_connect = None
    setting_buff = None
    attack_icon = None


    do_buff_detect = True
    do_hunt_detect = True
    do_magic_detect = True
    do_hunt_move = True
    def __init__(self,serial_connect,setting_buff):
        self.serial_connect = serial_connect
        self.setting_buff = setting_buff
        
    def randomPause(self,start,end):
        _start = int(start * 1000)
        _end = int(end * 1000)
        sec = randint(_start,_end) / 1000.0
        time.sleep(sec)
    
    #버프찾기 ...사용하는 버프를 못찾으면 isStatus를 수정한다. 전체 탐색 이후 버프사용로직을 실행한다.
    def onLoopDetect(self,ObserveStatus,buffWrap):
        while True:
            if self.setting_buff.useSaveFood:
                ObserveStatus.isSaveFood = detectBuff('imgName',buffWrap)
            if self.setting_buff.useSmallHwan:
                ObserveStatus.isSmallHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useMiddleHwan:
                ObserveStatus.isMiddleHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useBigHwan:
                ObserveStatus.isBigHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useTaeHwan:
                ObserveStatus.isTaeHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useGeukHwan:
                ObserveStatus.isGeukHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useTaegeukHwan:
                ObserveStatus.isTaegeukHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useSquireDuck:
                ObserveStatus.isSquireDuck =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useRainbowDcuk:
                ObserveStatus.isRainbowDcuk =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useEnergyStone:
                ObserveStatus.isEnergyStone =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useExp:
                ObserveStatus.isExp =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useGoonzuMentality:
                ObserveStatus.isGoonzuMentality =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useWorldHwan:
                ObserveStatus.isWorldHwan =  detectBuff('imgName',buffWrap)
            if self.setting_buff.useLetter:
                ObserveStatus.isLetter =  detectBuff('imgName',buffWrap)
            print('버프확인')
            self.randomPause(30,60)
    
    
    def onLoopSerialRead(self,ser):
        while True:
            if ser.readable():
                res = ser.readline().decode()
                self.proccessingDetect(res)
                print(res)
    
    def onLoopSocketIoRead(self,soc):
        soc.onLoadSocket()

    def onLoopHealth(self,healthWrap):
        while True:
            if self.setting_buff.useHealth:
                if self.setting_buff.useHealth > detectHealth(healthWrap):
                    actionHealth(self.serial_connect,healthWrap)
            self.randomPause(0.3,0.8)

    def setAttackIcon(self,attack_icon):
        self.attack_icon = attack_icon


    def onLoopMain(self,huntWrap):
        self.isStarted = True
        cursor_info = M_cursor()
        detectHunt = DetectHunt()
        x_center = (int)(huntWrap.CLIENT_X_POSITION + (huntWrap.CLIENT_WIDTH / 2))
        y_center = (int)(huntWrap.CLIENT_Y_POSITION + (huntWrap.CLIENT_HEIGHT / 2))
        center = [x_center,y_center]
        detect_wrap = [550,410]
        x_limit,y_limit = detect_wrap
        x_center,y_center = center

        block = 60

        block_x = 1
        block_y = 1
        block_area = 1
        block_x_limit = int(x_limit/block)+1
        block_y_limit = int(y_limit/block)+1
        #[x,y,방향] 8방좌표 시계방향
        while True:
            if self.setting_buff.useHunt:
                huntWrap.is_detect = detectHunt.do_detectHunt(cursor_info)
                if huntWrap.is_detect:
                    if self.do_hunt_detect:
                        time.sleep(0.5)
                        if detectHunt.do_detectHunt(cursor_info):
                            self.do_hunt_detect = False
                            actionHunt(self.serial_connect)
                            current_x, current_y = pyautogui.position()
                            if (not ((detect_wrap[0] + x_center) < current_x < (detect_wrap[0] - x_center)) or
                                    not ((detect_wrap[1] + y_center) < current_x < (detect_wrap[1] - y_center))):
                                block_x = 1
                                block_y = 1
                                block_area = 1
                            self.randomPause(1.0, 1.5)
                else :
                    if self.do_hunt_move :
                        if self.do_hunt_move and self.do_hunt_detect:
                            self.do_hunt_move = False
                            if (abs(block_x) == abs(block_y)) and block_area == 4:
                                block_x += 1
                            else:
                                if block_area == 1:
                                    block_x -= 1
                                elif block_area == 2:
                                    block_y -= 1
                                elif block_area == 3:
                                    block_x += 1
                                elif block_area == 4:
                                    block_y += 1
                                if abs(block_x) == abs(block_y): block_area += 1
                                if block_area == 5: block_area = 1
                            x_position = x_center + (block_x * block)
                            y_position = y_center + (block_y * block)
                            if block_x > block_x_limit and block_y > block_y_limit:
                                block_x = 1
                                block_y = 1
                                block_area = 1
                            actionMoveForTarget(self.serial_connect, x_position, y_position)

    def proccessingDetect(self,res):
        flag_cont = res[0:2]
        flag = flag_cont == '>>'
        if flag_cont == '<<' or flag_cont == '>>':
            resCont = res.split('|')[1].replace('\r\n','')
            if resCont == 'move':
                self.do_hunt_move = flag
            elif resCont ==  'click':
                self.do_hunt_detect = flag
            elif resCont == 'magic':
                self.do_magic_detect = flag

