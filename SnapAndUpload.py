import cv2
import dropbox
import random
import time

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        result = False
    
    return image_name
    print("Snap Is Taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()


def uploadPhoto(img_name):
    access_token = 'NfwQ_Itd6uUAAAAAAAAAAU3pyTDeZ1uA6AHAHH2GbMoF6jAQXjhxJ2cmi_-sxpHV'
    dbx = dropbox.Dropbox(access_token)

    file_from = img_name
    file_to = "/"+img_name

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Is Uploaded")



def main():
    while(True):
        if((time.time()- start_time)>= 5) : 
            name = take_snapshot()
            uploadPhoto(name)


main()
