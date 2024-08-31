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

while True:
    packet,_=client_socket.recvfrom(BUFF_SIZE)
    data=base64.b64decode(packet)
    npdata=np.frombuffer(data,dtype=np.uint8)
    frame=cv2.imdecode(npdata,1)
    cv2.imshow("Receiving Video ",frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        client_socket.close()
        break

