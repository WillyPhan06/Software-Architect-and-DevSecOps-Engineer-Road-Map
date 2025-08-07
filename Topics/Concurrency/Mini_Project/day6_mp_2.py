#Applying ProcessPoolExecutor to resize images from folder to output folder, Size is (width,height)
import os
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
import time

# Folder paths
INPUT_FOLDER = r"C:\Users\YourName\File\many_dawgs"
OUTPUT_FOLDER = r"C:\Users\YourName\File\output_many_dawgs"

# Resize to 300x300
SIZE = (300, 300)

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def resize_image(filename):
    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    try:
        task_start = time.time()
        with Image.open(input_path) as img:
            img = img.resize(SIZE)
            img.save(output_path)
            print(f"✅ Resized {filename} in {time.time() - task_start:.2f} seconds")
    except Exception as e:
        print(f"❌ Failed to process {filename}: {e}")


if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith((".jpg", ".png"))]
    start = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(resize_image, files)

    print(f"🎉 All images resized in {time.time() - start:.2f} seconds")
