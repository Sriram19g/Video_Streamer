import cv2,socket,time,base64,numpy as np

BUFF_SIZE=65536
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
print(host_ip)