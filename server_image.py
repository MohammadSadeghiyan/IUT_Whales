import socket
import numpy as np
import cv2
import os

MAX_DGRAM = 2**16-64
save_directory = '/mnt/d/udp'


def make_directory():
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)


def get_image(udp_socket):
    while True:
        print("Waiting for data...")

       
        file_name_bytes, client_address = udp_socket.recvfrom(MAX_DGRAM)
        file_name = file_name_bytes.decode('utf-8')
        print(f"Received file name: {file_name} from {client_address}")

        image_data = b''

        while True:
            img_bytes, _ = udp_socket.recvfrom(MAX_DGRAM)
            image_data += img_bytes
            if len(img_bytes) < MAX_DGRAM:
                break

        nparr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if frame is not None:
            file_path = os.path.join(save_directory, file_name)
            cv2.imwrite(file_path, frame)
            print(f"Image saved at {file_path}")
        else:
            print("Failed to decode image")


def excute_server_image(server_address):
    make_directory()
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(server_address)
    print(f"Server started at {server_address[0]}:{server_address[1]}")

    try:
        get_image(udp_socket)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cv2.destroyAllWindows()
        udp_socket.close()


