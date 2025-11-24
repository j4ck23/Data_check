import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def calculate_percent_difference(base_img, comparison_img):
    """
    Calculate the percent difference between the base image and comparison image.
    Uses Mean Squared Error (MSE) to quantify difference and converts it into percentage.
    """
    # Ensure both images have the same size
    if base_img.shape != comparison_img.shape:
        raise ValueError("The images must have the same dimensions")

    # Compute the squared difference
    diff = cv2.absdiff(base_img, comparison_img)
    diff_squared = diff.astype(np.float32)**2
    
    # Compute the mean squared error (MSE)
    mse = np.mean(diff_squared)
    
    # Normalize the MSE to a percentage
    max_possible_value = 255 ** 2  # max squared difference for pixel values in [0, 255]
    percent_diff = (mse / max_possible_value) * 100
    
    return percent_diff

def generate_heatmap(base_image_path, images_directory):
    """
    Generate a heatmap of the percent differences between the base image and other images in the directory.
    """
    # Read the base image
    base_img = cv2.imread(base_image_path, cv2.IMREAD_COLOR)
    base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)  # Convert to RGB for plotting
    
    # List all the image files in the directory
    image_files = [f for f in os.listdir(images_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    differences = []
    image_names = []
    
    # Iterate through the images in the directory
    for image_name in image_files:
        image_path = os.path.join(images_directory, image_name)
        comparison_img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        comparison_img = cv2.cvtColor(comparison_img, cv2.COLOR_BGR2RGB)
        
        try:
            # Calculate percent difference for each image
            percent_diff = calculate_percent_difference(base_img, comparison_img)
            differences.append(percent_diff)
            image_names.append(image_name)
        except ValueError as e:
            print(f"Skipping {image_name}: {e}")
    
    # Create a heatmap plot
    plt.figure(figsize=(10, 6))
    plt.imshow(np.array(differences).reshape(1, -1), cmap='hot', aspect='auto')
    plt.colorbar(label='Percent Difference')
    plt.xticks(ticks=np.arange(len(image_names)), labels=image_names, rotation=90)
    plt.yticks([])  # No y-axis ticks
    plt.title('Heatmap of Percent Differences between Base Image and Other Images')
    plt.savefig("Heat_map_Example")
    plt.show()

# Usage example
base_image_path = 'Unsimilar_Images/frame_0001.jpg'
images_directory = 'Unsimilar_Images'

generate_heatmap(base_image_path, images_directory)