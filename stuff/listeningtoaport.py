import socket
IP = "0.0.0.0"
#0.0.0.0 mtlb hum sabhi port par sunn rahe hai
PORT = 9090
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))
while True:
   data,(IP,PORT) = sock.recvfrom(1024)
   print("Sender: {} and PORT: {}".format(IP,PORT))
   print("Received message: {}".format(data))
