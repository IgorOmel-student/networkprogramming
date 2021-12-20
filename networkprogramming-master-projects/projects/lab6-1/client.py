import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

def send_to_server(ip, port):
    while True:
        send_data = input("Type some text to send =>");
        sock.sendto(send_data.encode('utf-8'), (ip, port))
        print("\n\n 1. Client Sent : ", send_data, "\n\n")
        data, address = sock.recvfrom(4096)
        print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 4242
    send_to_server(ip, port)
