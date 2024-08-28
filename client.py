import socket,cv2,pickle, struct
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_ip=input("Enter the HOST_IP     : ")
port=input("Enter the port number : ")

socket_addr=(host_ip,port)

client_socket.connect(socket_addr)

