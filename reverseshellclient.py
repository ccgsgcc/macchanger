import socket

rshell = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOCK_STREAM)
rshell.sendto(b'<Your message>', ('127.0.0.1', 8888))

