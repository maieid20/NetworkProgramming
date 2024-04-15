import socket
import threading

host = '127.0.0.1'
port = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = {}

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message to {client}: {e}")

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[client]
        broadcast(f'{nickname} left!'.encode('ascii'), client)
        clients.remove(client)
        del nicknames[client]
        client.close()

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames[client] = nickname
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'), client)
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
def main():
    while True:
        receive()

if __name__ == "__main__":
    main()
