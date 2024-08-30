import os,cv2,socket,time,base64,numpy as np,pickle

BUFF_SIZE=65536
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)


host_ip=socket.gethostbyname(socket.gethostname())
server_ip=input("Enter the server ip  : ")
server_port=int(input("Enter the port : "))
server_addr=(server_ip,server_port)
print(host_ip)
message=b"Hello"
sysname=os.uname().nodename
username=os.getlogin()

user=pickle.dumps((host_ip,sysname,username))

client_socket.sendto(user,server_addr)
