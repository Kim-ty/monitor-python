import configparser

properties = configparser.ConfigParser()
properties.read('./config.ini',encoding='utf-8')

serial_config = properties['SERIAL_INFO']
socket_config = properties['SOCKET_INFO']
hunt_config = properties['HUNT_INFO']

serial_port = serial_config['port']
baudRate = serial_config['baudRate']

socket_port = socket_config['port']
socket_host = socket_config['host']

max_attack_range = hunt_config['max_attack_range']
min_attack_range = hunt_config['min_attack_range']
use_auto_move = hunt_config['use_auto_move']