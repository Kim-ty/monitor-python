from wrap.global_wrap import INVEN_X_POSITION, INVEN_Y_POSITION, INVEN_WIDTH, INVEN_HEIGHT
from wrap.s_wrap import S_wrap


class Inven(S_wrap):
    def __init__(self,client):
        super(Inven ,self).__init__(client)
        self.x_position = INVEN_X_POSITION
        self.y_position = INVEN_Y_POSITION
        self.width = INVEN_WIDTH
        self.height = INVEN_HEIGHT