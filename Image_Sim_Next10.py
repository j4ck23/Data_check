from skimage.metrics import structural_similarity
import cv2
import os

Scores = []
images = 'Images_From_Video'
exts = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
all_files = [os.path.join(images, f) for f in os.listdir(images) if f.lower().endswith(exts)]
count = 0
print(type(all_files))

#Stop before last image
while count < len(all_files):
    for i in all_files:#For every image in list - I is current image
        count = count + 1
        ref_img = cv2.imread(i)#Reads image
        ref_grey = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)#Converts to grey
        for l in range(10):#For every image after current image
            compare = all_files[count + l]#Finds image path
            img = cv2.imread(compare)#Reads image
            img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Convert to grey

            score, _ = structural_similarity(ref_grey, img_grey, full=True)#Gets simularity score between images
            Scores.append((compare, score))#Appends
            
            print(f"SSIM between {i} and {compare}: {score:.4f}")


print("Image Similarity Scores:")
for img, score in Scores:
    print(f"{img}: {score:.4f}")