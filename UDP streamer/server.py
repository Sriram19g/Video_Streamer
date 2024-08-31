import cv2,socket,time,base64,numpy as np,pickle,imutils

BUFF_SIZE=65536
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

host_name=socket.gethostname()
host_ip=socket.gethostbyname(host_name)
port=2006
socket_addr=(host_ip,port)
server_socket.bind(socket_addr)
print(f"Listening at : {socket_addr}")

vid=cv2.VideoCapture('nature.mp4')
fps,st,frame_to_count,cnt=(0,0,20,0)

while True:
    info,client_addr=server_socket.recvfrom(BUFF_SIZE)
    info=pickle.loads(info)
    space=" "*5
    print(f"Got connection from {info[0]}{space}{info[1]}-->{info[2]} ")
    
    if not vid.isOpened():
        print("Can't Open file")
        continue
    WIDTH=500
    while (vid.isOpened()):
        ret,frame=vid.read()
        if not ret: 
            break
        frame=imutils.resize(frame,width=WIDTH)
        encoded,buffer=cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
        message=base64.b64encode(buffer)
        server_socket.sendto(message,client_addr)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            server_socket.close()
            break
    vid.release()

cv2.destroyAllWindows()










