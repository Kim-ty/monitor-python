# import json
#
# import socketio
# from config import socket_host, socket_port
#
# START_FLAG = 0
#
# sio = socketio.Server()
#
# @sio.on('message')
# def message(sid, data):
#     print('Client:[GET] : ', data)
#     result = json.loads(data)
#     global START_FLAG
#     START_FLAG = result['data']['start']
#     sio.send('{"isOk":1}')
#
#
#
# @sio.event
# def connect(sid, environ):
#     print('Client:Connect : ', sid)
#
#
# class Connect_socket:
#     sio = None
#
#     def __init__(self):
#         self.sio = sio
#         self.app = socketio.WSGIApp(self.sio, static_files={
#             '/': {'content_type': 'text/html', 'filename': 'index.html'}
#         })
#
#     def onLoadSocket(self):
#         socketio.server.SocketIOServer((socket_host, int(socket_port)), self.app).serve_forever()
#
#     def send(msg):
#         print('Client:[SEND] : ', msg)
#         sio.send(msg)