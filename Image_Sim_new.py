from skimage.metrics import structural_similarity
import cv2
import os


def img_sim(path, dest):
    Scores = []
    images = path
    dest_folder = dest
    exts = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
    all_files = [os.path.join(images, f) for f in os.listdir(images) if f.lower().endswith(exts)]
    dropped_image = 0 #Stores the amount of images dropped due to similarity
    chunks = [all_files[x:x+30] for x in range(0, len(all_files), 30)] #splits the files into smaller chunks for comparion
    #chnage the 30 to chnage chunk sze - 30 was chose as that is the most common frames per second of videos
    cycle = 0
    print(f"There are {len(chunks)} chunks")

    for chunk in chunks:
        count = 0
        cycle = cycle+1
        print(f"Chunk number: {cycle}")
        print(f"Number of images in chunk: {len(chunk)}")
        while count < len(chunk):
            for i in chunk:
                count = count + 1
                sim = False # Similarity check
                ref_img = cv2.imread(i)
                ref_grey = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
                Sim_scores = []#List to store similiarty scores, recreated with every new refernce image
                for l in range(len(chunk) - count):
                    compare = chunk[count + l]
                    img = cv2.imread(compare)
                    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                    score, _ = structural_similarity(ref_grey, img_grey, full=True)
                    Sim_scores.append(score)
                    
                    print(f"SSIM between {i} and {compare}: {score:.4f}")
                for j in Sim_scores:
                    if j > 0.8000:
                        sim = True
                    else:
                        continue
                if sim == False:
                    Scores.append(i)
                    name = i.split('/')[1]
                    name = name.split('.')[0]
                    filename = os.path.join(dest_folder, f"{name}.jpg")
                    cv2.imwrite(filename, ref_img)
                else:
                    dropped_image = dropped_image + 1


    """
    print("Image Similarity Scores:")
    for img, score in Scores:
        print(f"{img}: {score:.4f}")
    """

    print(f"images in count: {len(Scores)}")
    print(f"Number of images dropped due to similarity: {dropped_image}")

    return len(Scores), dropped_image


quality_dest = 'Images_From_Video'#Set dest for quality assessent and similiarty path
sim_dest = 'Unsimilar_Images'#Set dest for similiarity comparions

img_sim(quality_dest, sim_dest)