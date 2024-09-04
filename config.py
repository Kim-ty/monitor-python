import configparser

properties = configparser.ConfigParser()
properties.read('./config.ini',encoding='utf-8')

path_config = properties['PATH']
serial_config = properties['SERIAL_INFO']
socket_config = properties['SOCKET_INFO']


serial_port = serial_config['port']
baudRate = serial_config['baudRate']

socket_port = socket_config['port']
socket_host = socket_config['host']