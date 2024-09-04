from PIL import Image
from sympy.stats.sampling.sample_numpy import numpy


class M_cursor:

    attack_cursor = None
    select_cursor = None

    def __init__(self):
        self.attack_bmp = Image.open('./img/attack.bmp')
        self.select_bmp = Image.open('./img/select.bmp')
        self.attack_np = numpy.array(self.attack_bmp)
        self.select_np = numpy.array(self.select_bmp)