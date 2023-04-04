## Ig_post_resizer
Ig_post_resizer is a Python program that resizes images to the allowed format of Instagram posts by adding a white squared canvas and centering the images inside it, without losing quality. This repository contains the source code for this program.

## Instalation
To use Ig_post_resizer, you will need to have Python installed on your machine. You can clone the repository using the following command:

    git clone https://github.com/AlvaroNovillo/Ig_post_resizer.git
    
    
## Usage
Once you have downloaded the code, navigate to the project directory and launch the Ig_post.exe app located inside the dist folder. This will open a window giving you the option to select the folder where the pictures are located, and to add a watermark. After you have selected the folder, press the button Process images and the program will automatically resize all images and save them to a new folder called IG within the original folder.

Make sure to change the watermark.png file to the desired watermark to add. Note that his feature is in an early stage of development and the results may not be perfect

## About the Program
This program uses the Python Imaging Library (PIL) to manipulate the images. It creates a canvas with a fixed size based on the image size. It then resizes the original image and pastes it onto the center of the canvas. If the original image is a landscape photo, it calculates the left and right borders to add to the canvas. If the original image is a vertical photo, it calculates the top and bottom borders to add. Finally, it saves the resized image to the output folder.

Right now the program is optimized for either landscape oriented and vertical images.


## About Me

I'm a humble physicist trying to learn about Python and Data Science. If you want to contact me don't doubt to use my linkedin:
* <div class="badge-base LI-profile-badge" data-locale="es_ES" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="álvaro-novillo-correas-1b4452226" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://es.linkedin.com/in/%C3%A1lvaro-novillo-correas-1b4452226?trk=profile-badge">Álvaro Novillo Correas</a></div>
