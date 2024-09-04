from wrap.global_wrap import HEALTH_X_POSITION, HEALTH_WIDTH, HEALTH_HEIGHT, HP_Y_POSITION, MP_Y_POSITION
from wrap.s_wrap import S_wrap


class Health(S_wrap):
    end_x_position = None
    end_y_position = None
    def __init__(self,client,y_point):
        super(Health ,self).__init__(client)
        self.x_position = HEALTH_X_POSITION
        self.y_position = y_point
        self.width = HEALTH_WIDTH
        self.height = HEALTH_HEIGHT
        self.end_x_position = self.x_position + self.width
        self.end_y_position = self.y_position + self.height



class Hp(Health):

    type='hp'

    def __init__(self,client):
        super(Hp,self).__init__(client,HP_Y_POSITION)



class Mp(Health):
    type = 'mp'
    def __init__(self,client):
        super(Mp,self).__init__(client,MP_Y_POSITION)