import threading
import socket


class Broker():

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', 4242))
        self.clients_list = []

    def talkToClient(self, ip):
        answer = input('Type to answer')
        self.sock.sendto(answer.encode('utf-8'), ip)

    def listen_clients(self):
        while True:
            msg, client = self.sock.recvfrom(1024)
            t = threading.Thread(target=self.talkToClient, args=(client,))
            t.start()

if __name__ == '__main__':
    b = Broker()
    b.listen_clients()
