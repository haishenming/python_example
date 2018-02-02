import socket

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('Server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('Connected by ', addr)

    while True:
        data = conn.recv(1024)
        print(data.decode("utf-8"))

        conn.sendall("server received you message.".encode("utf-8"))

# conn.close()
