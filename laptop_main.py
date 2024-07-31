import server_control
import server_image
import socket
from threading import Thread


def get_ip_server_address():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr


server_ip='127.0.0.1'
server_control_port=1234
server_image_port=12345
server_control_address=(server_ip,server_control_port)
server_image_address=(server_ip,server_image_port)


rass_ip='127.0.0.1'

def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_control.send_info(udp_socket,server_control_address)
    udp_socket.close()
    while True:
        server_control.excute_server_control(server_control_address)
        thread=Thread(target=server_image.excute_server_image,args=(server_image_address,))
        thread.start()
if __name__=="__main__":
    main()
