try:
    from PIL import Image
except ImportError:
    raise ImportError("Pillow is not installed. Run 'python3 -m pip install Pillow' to install it")
from random import randint
from time import time
import os

#settings for the random shift of the image
shiftfreq = 300
maxshiftamount = 250
minshiftamount = 0

#rotation settings for the image    
rotatebeforeamount = 0
rotateafteramount = 3

# Name of the image to be processed and the name of the image to be saved
imagename = "Image.jpg"
returnedimagename = "Returnedimage.jpg"


## anything below this, dont touch xD
## funny rotate function
def rotate(im, times):
    print (f"Rotating image {times} times")
    for i in range(times):
        im = im.transpose(Image.ROTATE_90)
    return im
## get the path of the file
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("\\", "/") + "/"
# Open the image
im = Image.open(f"{path}{imagename}")
# Rotate the image
im = rotate(im, rotatebeforeamount)
# Create a new image to return
returnedimage = Image.new("RGB", (im.size[0], im.size[1]), "white")
# Get the size of the image
width, height = im.size
print (f"Processing image of Width: {width}, Height: {height}")
randomshift = 0
# Process every row of the image
for x in range(0, height):
    if x % int(height/shiftfreq) == 0:
        randomshift = randint(minshiftamount, maxshiftamount)
        randomshiftdir = randint(0, 1)
    # Create a list of the pixels in the row
    row = []
    for y in range(0, width):
        # Get the pixel
        pixel = im.getpixel((y, x))
        row.append(pixel)
    # Shift the row   
    for i in range(0,randomshift):
        if randomshiftdir == 0:
            row.append(row.pop(0))
        else:
            row.insert(0, row.pop())
    # Put the row back into the image
    for y in range(0, width):
        returnedimage.putpixel((y, x), row[y])
# Rotate the image
returnedimage = rotate(returnedimage, rotateafteramount)
# Save the image
print ("Saving image")
returnedimage.save(f"{path}{returnedimagename}")
print ("Image saved")
## show the image
image = Image.open(f"{path}{returnedimagename}")
image.show()