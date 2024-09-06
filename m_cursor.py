from random import randint

import numpy
from PIL import Image

from config import max_attack_range, min_attack_range


class M_cursor:

    attack_cursor = None
    select_cursor = None
    #본인포함
    attack_range = max_attack_range
    min_attack_range = min_attack_range


    def __init__(self):
        self.attack_bmp = Image.open('./img/attack.bmp')
        self.select_bmp = Image.open('./img/select.bmp')
        self.attack_np = numpy.array(self.attack_bmp)
        self.select_np = numpy.array(self.select_bmp)
        self.block_to_x_pos = 0
        self.target_block_y = 0

    def block_to_valid(self,block_arr):
        x_pos, y_pos = block_arr
        if ((abs(x_pos) + abs(y_pos)) % 2 != 0) or (abs(x_pos) + abs(y_pos) > self.attack_range * 2):
            return False

        return True

    #x+y가 홀수면 탈락 attack_range를 *2 하여 마름모의 절반 단위로 계산
    def block_to_pos(self,block_arr):
        x_pos,y_pos = block_arr

        return [x_pos*40,y_pos*20]

    def generate_mouse_block(self):
        block_limit = self.attack_range * 2
        block_min_limit = self.min_attack_range * 2
        while True:
            x_pos = randint(2, self.attack_range*2)
            y_pos = randint(2, self.attack_range*2)
            if min_attack_range < x_pos+y_pos <= block_limit and (x_pos+y_pos)%2 == 0:
                return [x_pos,y_pos]