import socket
import threading


def recv_msg(udp_server):
    while True:
        recv = udp_server.recvfrom(1024)
        print(recv[0].decode('utf-8'))
        # udp_server.close()


def send_msg(udp_server, host, port):
    while True:
        send = input("please input:")
        udp_server.sendto(send.encode('utf-8'), (host, port))
        # udp_server.close()


def main():
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = socket.gethostname()

    myPort = 5500
    yourPort = 5000

    udp_server.bind((host, myPort))

    t1 = threading.Thread(target=recv_msg, args=(udp_server,))
    t2 = threading.Thread(target=send_msg, args=(udp_server, host, yourPort))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
