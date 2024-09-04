from wrap.global_wrap import HUNT_X_POSITION, HUNT_Y_POSITION
from wrap.s_wrap import S_wrap


class Hunt(S_wrap):
    is_detect = 0
    end_x_position = None
    end_y_position = None
    def __init__(self,client):
        super(Hunt ,self).__init__(client)
        self.x_position = HUNT_X_POSITION
        self.y_position = HUNT_Y_POSITION
        self.width = 640
        self.height = 640
        self.end_x_position = self.x_position + self.width
        self.end_y_position = self.y_position + self.height
