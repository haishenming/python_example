import socket
HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = input("Please input msg:")
    s.send(cmd.encode("utf-8"))
    data = s.recv(1024)
    print(data.decode("utf-8"))

# s.close()