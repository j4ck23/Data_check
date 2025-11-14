from split_new import split_one_frame_per_second as split
from img_assess import quality
from skimage.metrics import structural_similarity
import cv2
import numpy as np

if __name__ == "__main__":
    split_dest = 'Images'
    quality_dest = 'Images_From_Video'
    video = "GX010629.MP4"
    split(video, split_dest) #Splits video into frames
    quality(split_dest,quality_dest) #Checks the quality of each frame (Sharpness, brightness)

