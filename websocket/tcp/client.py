import socket
HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input("Please input msg:")
    s.sendto(cmd.encode("utf-8"), (HOST, PORT))
    data, flag = s.recvfrom(1024)
    print(data.decode("utf-8"))

# s.close()