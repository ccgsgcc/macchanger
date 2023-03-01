import socket

rshell = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOCK_STREAM)
rshell.bind(('127.0.0.1', 8888))

result = rshell.recv(1024)
print('Message:', result.decode('utf-8'))
rshell.close()
