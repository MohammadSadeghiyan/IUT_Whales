import socket

FORMAT = 'UTF-8'

def get_substring_after_colon(input_string):
    parts = input_string.split(':', 1)
    return parts[1] if len(parts) > 1 else ''

def get_info_from_laptop(udp_socket):
    print("Waiting for data from laptop...")
    data_bytes, _ = udp_socket.recvfrom(2048)
    print("Data received.")
    print(data_bytes.decode(FORMAT))
    data = get_substring_after_colon(data_bytes.decode(FORMAT))
    print(data)

def excute_client_control(client_address):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(client_address)
    # send_info_from_rasberry(udp_socket)
    get_info_from_laptop(udp_socket)
    udp_socket.close()


