from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.connect((host, port))

    while True:
        message = input("client: ")
        message_length = len(message)
        s.send(str(message_length).encode('utf-8'))
        s.send(b'\n')  
        s.send(message.encode('utf-8'))

        response_length = int(s.recv(1024).decode('utf-8'))
        response = b''
        while len(response) < response_length:
            chunk = s.recv(1024)
            if not chunk:
                break
            response += chunk
        print("server:", response.decode('utf-8'))

    s.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat terminated")
