import PIL
from PIL import Image
import os

mywidth = 300
source_dir = r"C:\Users\asus\OneDrive\Pictures\Camera Roll"
destination_dir = r"C:\Users\asus\OneDrive\Pictures\Camera\destination"

def resize_pic(old_pic, new_pic):
    try:
        img = Image.open(old_pic)
    except (PIL.UnidentifiedImageError, OSError):
        print(f"Skipping non-image file: {old_pic}")
        return

    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth, hsize), PIL.Image.LANCZOS)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(new_pic), exist_ok=True)

    img.save(new_pic)

def entire_directory(source_dir, dest_dir):
    files = os.listdir(source_dir)
    i = 0
    for file in files:
        i += 1
        old_pic = os.path.join(source_dir, file)
        new_pic = os.path.join(dest_dir, file)

        print("old_pic: ", old_pic)
        print("new_pic: ", new_pic)
        resize_pic(old_pic, new_pic)
        print(i, "done")

entire_directory(source_dir, destination_dir)
