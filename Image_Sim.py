from skimage.metrics import structural_similarity
import cv2
import os

Scores = []
images = 'Images_From_Video'
exts = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
all_files = [os.path.join(images, f) for f in os.listdir(images) if f.lower().endswith(exts)]
count = 0
print(type(all_files))

while count < len(all_files):
    for i in all_files:
        count = count + 1
        print(count)
        ref_img = cv2.imread(i)
        ref_grey = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
        for l in range(len(all_files) - count):
            compare = all_files[count + l]
            img = cv2.imread(compare)
            img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            score, _ = structural_similarity(ref_grey, img_grey, full=True)
            Scores.append((compare, score))
            
            print(f"SSIM between {i} and {compare}: {score:.4f}")


print("Image Similarity Scores:")
for img, score in Scores:
    print(f"{img}: {score:.4f}")