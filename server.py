import socket,cv2,pickle,struct

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_name=socket.gethostbyname()
host_ip=socket.gethostbyname(host_name)
print("HOST IP : ",host_ip)
port=8888
socket_addr=(host_ip,port)

server_socket.bind(socket_addr)
server.socket.listen(5)
print("LISTENING AT: ",socket_addr)



