import cv2

def take_picture():
    
    webcam = cv2.VideoCapture(0)


    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    check, frame = webcam.read()
    if check:
    
        img_filename = 'captured_image.jpg'
        cv2.imwrite(img_filename, frame)
        print(f"Image saved as {img_filename}")
    else:
        print("Failed to grab frame")


    webcam.release()
    cv2.destroyAllWindows()
    