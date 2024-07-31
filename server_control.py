import socket
import subprocess
import re


FORMAT = 'UTF-8'



def get_info(udp_socket):
    pass


def send_info(udp_socket,client_control_address):
    data_send = "location:"
    data_send += input("please take location: ")
    udp_socket.sendto(data_send.encode(FORMAT), client_control_address)

def excute_server_control(client_address):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # get_info(udp_socket)
    send_info(udp_socket,client_address)
    udp_socket.close()     

