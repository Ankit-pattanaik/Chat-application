#clientchat.py
import socket
while(True):
    s=socket.socket()
    s.connect(("127.0.0.1",4899))
    cddata=input("ANKIT:")
    if(cddata.lower()=="bye"):
        s.send("Bye Bro see you soon".encode())
        break
    else:
        s.send(cddata.encode())
        ssdata=s.recv(1024).decode()
        print("LEO:",ssdata)