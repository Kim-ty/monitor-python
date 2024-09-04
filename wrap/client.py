import pyautogui
import win32gui

from wrap.global_wrap import PROCESS_CLASS_NAME


class Client:

    CLIENT_X_POSITION = 0
    CLIENT_Y_POSITION = 0
    CLIENT_WIDTH = 0
    CLIENT_HEIGHT = 0

    def __init__(self):
        def callback(_hwnd, _result: list):
            title = win32gui.GetWindowText(_hwnd)
            if win32gui.IsWindowEnabled(_hwnd) and win32gui.IsWindowVisible(_hwnd) and title is not None and len(
                    title) > 0:
                _result.append(_hwnd)
            return True

        result = []
        win32gui.EnumWindows(callback, result)

        _hwnd = None

        for hwnd in result:
            if win32gui.GetClassName(hwnd) == PROCESS_CLASS_NAME:
                _hwnd = hwnd
                break

        if _hwnd is not None:
            hwnd_rect_tuple = win32gui.GetWindowRect(_hwnd)

            self.CLIENT_X_POSITION = hwnd_rect_tuple[0]
            self.CLIENT_Y_POSITION = hwnd_rect_tuple[1]
            self.CLIENT_WIDTH = hwnd_rect_tuple[2]-hwnd_rect_tuple[0]
            self.CLIENT_HEIGHT = hwnd_rect_tuple[3]-hwnd_rect_tuple[1]

            win32gui.SetForegroundWindow(_hwnd)

        print(self.CLIENT_X_POSITION, self.CLIENT_Y_POSITION)
        print(self.CLIENT_WIDTH, self.CLIENT_HEIGHT)



