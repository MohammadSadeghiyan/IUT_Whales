import client_control
import client_image
import get_image
import socket

client_control_port=1234
client_image_port=12345
client_ip='127.0.0.1'

def main():
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind((client_ip,client_control_port))
    client_control.get_info_from_laptop(udp_socket)
    udp_socket.close()
    #connection with stm and get the location of the robot and when we go on the sea send data for laptop
    
if __name__=="__main__":
    main()    
    