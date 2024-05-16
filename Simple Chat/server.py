from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 7002
    s.bind((host, port))
    s.listen(5)
    client, addr = s.accept()
    print("Connection from", addr[0])
    
    while True:
        message_length = int(client.recv(1024).decode('utf-8'))
        message = b''
        while len(message) < message_length:
            chunk = client.recv(1024)
            if not chunk:
                break
            message += chunk
        print("Client:", message.decode('utf-8'))
        
        response = input("Server: ")
        response_length = len(response)
        client.send(str(response_length).encode('utf-8'))
        client.send(b'\n') 
        client.send(response.encode('utf-8'))

    client.close()

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat terminated")
s.close()
