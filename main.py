#무조건 cmd 관리자로해야함, main.spec가 있으니 1번 명령어는 필요없음.
#1. pyinstaller -F --add-data "./img/*;./img" --add-data "config.ini;./" main.py
#2. pyinstaller main.spec



import sys
import threading
import time
import os

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
    print('Running in a PyInstaller bundle')
else:
    base_path = os.path.abspath(".")
    print('Running in a normal Python process')


from connect.con_serial import Connect_serial
# from connect.con_socket import Connect_socket



from observe import BuffStatus
from setting_model import SettingBuff
from thread import MonitorThreading
from wrap.buff import Buff
from wrap.client import Client
from wrap.health import Hp, Mp
from wrap.hunt import Hunt
from wrap.inven import Inven
from wrap.place import Place

expItem = [7,8,10,12]

buff_list = {
    'useHunt':1,
    'clickTiming':0.5,
    'useHealth':30,
    'useMagic' : 6,
    'useSmallHwan': 1,
    'useMiddleHwan': 1,
    'useBigHwan': 1,
    'useTaeHwan': 1,
    'useGeukHwan': 1,
    'useTaegeukHwan': 1,
    'useSquireDuck': 1,
    'useRainbowDcuk': 1,
    'useEnergyStone': 1,
    'useExp': 7,
    'useGoonzuMentality': 1,
    'useSaveFood': 1,
    'useWorldHwan': 1,
    'useLetter': 1,
}

def threadTest():
    for i in range(30):
        time.sleep(1)
    print('--------------------------------------------------------------------------------')

if __name__ == '__main__':

    # 선언부
    client = Client()

    if(client.CLIENT_WIDTH == 0 or client.CLIENT_HEIGHT == 0):
        print('클라를 탐지하지 못했습니다.')
        sys.exit()

    con_serial = Connect_serial()
    # con_soc = Connect_socket()
    setting_buff = SettingBuff(buff_list)
    buff_status = BuffStatus()
    monitor = MonitorThreading(con_serial,setting_buff)

    #범위지정
    wrap_hunt = Hunt(client)
    wrap_buff = Buff(client)
    wrap_hp = Hp(client)
    wrap_mp = Mp(client)
    wrap_place = Place(client)
    wrap_inven = Inven(client)

    detectBuffThread = threading.Thread(target=monitor.onLoopDetect,args=(buff_status,wrap_buff))
    huntDetectThread = threading.Thread(target=monitor.onLoopMain,args=(wrap_hunt,))
    recoverHpThread = threading.Thread(target=monitor.onLoopHealth,args=(wrap_hp,))
    recoverMpThread = threading.Thread(target=monitor.onLoopHealth,args=(wrap_mp,))
    serialReadThread = threading.Thread(target=monitor.onLoopSerialRead, args=(con_serial.ser,))
    # socketReadThread = threading.Thread(target=monitor.onLoopSocketIoRead, args=(con_soc,))

    detectBuffThread.daemon = True
    recoverHpThread.daemon = True
    recoverMpThread.daemon = True
    serialReadThread.daemon = True
    # socketReadThread.daemon = True

    # socketReadThread.start()

    # if setting_buff.monitor_start:
    serialReadThread.start()
    #버프로직 스타트
    detectBuffThread.start()
    # #회복로직 스타트 -------------완료
    recoverHpThread.start()
    recoverMpThread.start()

    monitor.onLoopMain(wrap_hunt)

    os.system('pause')