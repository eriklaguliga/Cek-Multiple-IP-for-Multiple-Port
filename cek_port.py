import socket
import os

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

print("Contoh input : 192.168.128.1,192.168.128.2,192.168.128.1")
print("Jika innput hanya satu IP cukup input :192.168.128.1 ")
ip = list(input("Enter a multiple ip or single ip: ").split(","))

print("                                                      ")
print("Contoh input : 443,4122,4120")
print("Jika innput hanya satu port cukup input :443")
port = list(map(int, input("Enter a multiple port or single port: ").split(",")))

for i in range(len(ip)):
    print("                        ")
    print("Scanning IP:",ip[i])
    for o in range(len(port)):
        # print(b[o])
        # print("Scanning IP",a[i], "FOR PORT:",b[o])
        if isOpen(ip[i], port[o]) == True:
            print("TCP port", port[o], ": Open")
        else:
            sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hasil = sv.connect_ex((ip[i], port[o]))
            if(hasil == 10061):
                print("TCP port", port[o], ": Not Listening")
            elif(hasil == 10060):
                print("TCP port", port[o], ": Filtered")
            else:
                print("your host is unreach")

