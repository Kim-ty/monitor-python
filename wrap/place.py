from wrap.global_wrap import PLACE_X_POSITION, PLACE_Y_POSITION,PLACE_WIDTH,PLACE_HEIGHT
from wrap.s_wrap import S_wrap


class Place(S_wrap):
    def __init__(self,client):
        super(Place ,self).__init__(client)
        self.x_position = PLACE_X_POSITION
        self.y_position = PLACE_Y_POSITION
        self.width = PLACE_WIDTH
        self.height = PLACE_HEIGHT