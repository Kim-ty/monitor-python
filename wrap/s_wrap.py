import pyautogui


class S_wrap:
    CLIENT_X_POSITION = 0
    CLIENT_Y_POSITION = 0
    CLIENT_WIDTH = 0
    CLIENT_HEIGHT = 0
    def __init__(self,client):
        self._do_detecting = None
        self._height = 0
        self._width = 0
        self._y_position = 0
        self._x_position = 0
        self.CLIENT_X_POSITION = client.CLIENT_X_POSITION
        self.CLIENT_Y_POSITION = client.CLIENT_Y_POSITION
        self.CLIENT_WIDTH = client.CLIENT_WIDTH
        self.CLIENT_HEIGHT = client.CLIENT_HEIGHT

    @property
    def x_position(self):
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        self._x_position = self.CLIENT_X_POSITION+2+value

    @property
    def y_position(self):
        return self._y_position

    @y_position.setter
    def y_position(self, value):
        self._y_position = self.CLIENT_Y_POSITION+1+value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def do_detecting(self):
        return self._do_detecting

    @do_detecting.setter
    def do_detecting(self, value):
        self._do_detecting = value

    def captureWrap(self,file_name):
        dest = "E:/test123123/"
        pyautogui.screenshot(dest+file_name+'.png',(self.x_position,self.y_position,self.width,self.height))