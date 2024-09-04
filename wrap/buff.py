from wrap.global_wrap import BUFF_X_POSITION, BUFF_Y_POSITION, BUFF_WIDTH, BUFF_HEIGHT
from wrap.s_wrap import S_wrap


class Buff(S_wrap):

    def __init__(self,client):
        super(Buff,self).__init__(client)
        self.x_position = BUFF_X_POSITION
        self.y_position = BUFF_Y_POSITION
        self.width = BUFF_WIDTH
        self.height = BUFF_HEIGHT
