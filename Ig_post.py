import os
import glob
from PIL import Image
import tkinter as tk
from tkinter import filedialog



# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Ask the user to select the folder containing the pictures
folder_path = filedialog.askdirectory(title='Please select the folder containing the pictures')

# Check if the user selected a folder
if not folder_path:
    print('No folder selected')
    exit()

# Get a list of all the pictures in the folder
picture_files = glob.glob(os.path.join(folder_path, '*.jpg'))

# Create the output folder
output_folder = os.path.join(folder_path, 'IG')
os.makedirs(output_folder, exist_ok=True)

# Loop through each picture and create an Instagram post

for picture_file in picture_files:
    # Open the picture
    picture = Image.open(picture_file)

    # Calculate the size of the canvas
    picture_width, picture_height = picture.size
    canvas_size = max(picture_width, picture_height)

    # Calculate the left and right borders for landscape photos
    if picture_width > picture_height:
        left_border = (canvas_size - picture_height) // 4
        right_border = left_border
        top_border = 0
        bottom_border = 0

    # Calculate the top and bottom borders for vertical photos
    elif picture_height > picture_width:
        top_border = (canvas_size - picture_width) // 4
        bottom_border = top_border
        left_border = 0
        right_border = 0
    else:
        top_border = 0
        bottom_border = 0
        left_border = 0
        right_border = 0

    # Create the canvas and paste the picture onto it
    canvas = Image.new('RGB', (canvas_size, canvas_size), color='white')
    x = (canvas_size - picture_width) // 2
    y = (canvas_size - picture_height) // 2
    canvas.paste(picture, (x, y))

    # Calculate the new size of the canvas with spacing
    new_canvas_size = canvas_size + left_border + right_border + top_border + bottom_border
    # Create a new canvas with spacing and paste the original canvas onto it
    new_canvas = Image.new('RGB', (new_canvas_size, new_canvas_size), color='white')
    x = (new_canvas_size - canvas_size) // 2
    y = (new_canvas_size - canvas_size) // 2
    new_canvas.paste(canvas, (x, y))

    # Save the image to disk
    output_file = os.path.join(output_folder, os.path.basename(picture_file))
    new_canvas.save(output_file, quality=100)
    
     # Save the image to disk
    output_file = os.path.join(output_folder, os.path.basename(picture_file))
    new_canvas.save(output_file, quality=100)

    # Print a message to indicate that the post has been created
    print('Created Instagram post for', picture_file)
