import os
import glob
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.title('Image Watermarking Tool')

# Create a frame for the checkbox and folder selection
top_frame = tk.Frame(root)
top_frame.pack(padx=20, pady=10)

# Create a simple GUI with a checkbox to decide whether to add the watermark or not
add_watermark = tk.BooleanVar()
checkbox = tk.Checkbutton(top_frame, text='Add watermark', variable=add_watermark)
checkbox.pack(side='left')

# Create a label for the selected folder path
folder_path_label = tk.Label(top_frame, text='No folder selected')
folder_path_label.pack(side='left', padx=10)

# Function to select a folder and update the label with the selected path
def select_folder():
    folder_path = filedialog.askdirectory(title='Please select the folder containing the pictures')
    if folder_path:
        folder_path_label.config(text=folder_path)
    

# Create a button to select the folder
select_folder_button = tk.Button(top_frame, text='Select folder', command=select_folder)
select_folder_button.pack(side='left')

# Function to process the images
def process_images():
    folder_path = folder_path_label.cget('text')
    if not folder_path:
        print('No folder selected')
        return
    
    add_watermark_value = add_watermark.get()
    
    # Get a list of all the pictures in the folder
    picture_files = glob.glob(os.path.join(folder_path, '*.jpg'))
    
    # Create the output folder
    output_folder = os.path.join(folder_path, 'IG')
    os.makedirs(output_folder, exist_ok=True)
    
    
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
            delta = 200
    
        # Calculate the top and bottom borders for vertical photos
        elif picture_height > picture_width:
            top_border = (canvas_size - picture_width) // 4
            bottom_border = top_border
            left_border = 0
            right_border = 0
            delta = 50
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
        
        if add_watermark_value:
            watermark_path = r'watermark.png'
            watermark = Image.open(watermark_path)
            watermark_width, watermark_height = watermark.size
            watermark = watermark.resize((watermark_width//2, watermark_height//2))
            x = new_canvas_size - watermark_width//2 - 10 - delta# 10px right margin
            y = new_canvas_size - watermark_height//2 - 15 - 2*delta # 10px bottom margin
            new_canvas.paste(watermark, (x, y), mask=watermark)
    
    
        # Save the image to disk
        output_file = os.path.join(output_folder, os.path.basename(picture_file))
        new_canvas.save(output_file, quality=100)
        
         # Save the image to disk
        output_file = os.path.join(output_folder, os.path.basename(picture_file))
        new_canvas.save(output_file, quality=100)
    
        # Print a message to indicate that the post has been created
        print('Created Instagram post for', picture_file)
    
    print('Images processed successfully')

# Create a button to start processing the images
process_images_button = tk.Button(root, text='Process images', command=process_images)
process_images_button.pack(pady=10)

# Start the main loop
root.mainloop()



    
# Loop through each picture and create an Instagram post


