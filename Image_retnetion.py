from split_new import split_one_frame_per_second as split
from img_assess import quality
from Image_Sim_new import img_sim
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    split_dest = 'Images'#Set the dest for images from video and quality assessment path
    quality_dest = 'Images_From_Video'#Set dest for quality assessent and similiarty path
    sim_dest = 'Unsimilar_Images'#Set dest for similiarity comparions
    video = "GX010629.MP4"#Video to get frames from
    split(video, split_dest) #Splits video into frames
    count = 0
    # Iterate directory
    for path in os.listdir(split_dest):
        # check if current path is a file
        if os.path.isfile(os.path.join(split_dest, path)):
            count =  count + 1

    qual = quality(split_dest,quality_dest) #Checks the quality of each frame (Sharpness, brightness)
    sim = img_sim(quality_dest,sim_dest)#Checks the similiarity between each frame and returns unquie frames
    
    
    #Prints some details about the video and frames
    percent = qual[0] / qual[1] * 100
    percent2 = qual[1] / sim[0]
    print("Details:")
    print(f'Video split into {count} frames')
    print(f"Images dropped due to clarity: {qual[1]-qual[0]}")
    print(f"Qualified images (Acceptable or Sharp and Normal exposure): {qual[0]} ({percent:.2f}%)")
    print(f"Number of images dropped due to similarity: {sim[1]}")
    print(f"Frames for anaylsis: {sim[0]} ({percent2:.2f}%)")