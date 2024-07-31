import os
import cv2
import socket

MAX_DGRAM = 2**16 - 64  
# folder path that contains image files
folder_path = '/mnt/d/object_detection' 

# split images into the little chunks
def split_image_bytes(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# find all .jpg files and return a list of the .jpg files
def find_jpg_files(fold_path):
    return [os.path.join(fold_path, f) for f in os.listdir(fold_path) if f.endswith('.jpg')]

def send_image(client_socket,server_address):
    jpg_files = find_jpg_files(folder_path)

    for image_path in jpg_files:
        file_name = os.path.basename(image_path)
        client_socket.sendto(file_name.encode(), server_address)  
        
        frame = cv2.imread(image_path)

        if frame is not None:
            print(f"Image {image_path} loaded successfully")
            _, buffer = cv2.imencode('.jpg', frame)
            image_bytes = buffer.tobytes()
            
            chunks = split_image_bytes(image_bytes, MAX_DGRAM)
            
            for chunk in chunks:
                client_socket.sendto(chunk, server_address)
                print(f"Sent chunk of size {len(chunk)} bytes from {image_path}")
            
            print(f"Image {image_path} sent successfully")
        else:
            print(f"Failed to load image {image_path}")

def excute_client_image(server_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Connecting to server at {server_address}")
    send_image(client_socket)
    client_socket.close()


