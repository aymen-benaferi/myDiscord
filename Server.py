import socket
import threading


class Server:
    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f'Server is running on {self.host}:{self.port}')

        while True:
            client_socket, client_address = self.server.accept()
            print(f'New connection from {client_address}')

            self.clients.append(client_socket)
            thread = threading.Thread(
                target=self.handle_client, args=(client_socket,))
            thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    self.remove_client(client_socket)
                    break
                print(f'Received message: {message}')
                self.broadcast(message)
            except Exception as e:
                print(f'Error: {e}')
                self.remove_client(client_socket)
                break

    def broadcast(self, message):
        for client_socket in self.clients:
            try:
                client_socket.sendall(message.encode())
            except Exception as e:
                print(f'Error: {e}')
                self.remove_client(client_socket)

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            client_socket.close()
            print('Client disconnected')


server = Server()
server.start()
