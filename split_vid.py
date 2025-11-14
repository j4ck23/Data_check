import cv2
import os

def split(x,dest):
    vidcap = cv2.VideoCapture(x)
    if vidcap.isOpened():
        path = dest
        success,image = vidcap.read()
        count = 0
        success = True

        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
            success,image = vidcap.read()
            cv2.imwrite(os.path.join(path, "frame%d.jpg") % count, image)    # save frame as JPEG file      
            count = count + 1