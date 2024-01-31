#serverchat.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",4899))
s.listen(2)
print("LEO IS READY TO CHAT WITH YOU")
while(True):
    cs,ca=s.accept()
    csdata=cs.recv(1024).decode()
    print("ANKIT:{}".format(csdata))
    ssdata=input("LEO:")
    cs.send(ssdata.encode())
