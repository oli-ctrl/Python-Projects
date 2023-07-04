from PIL import Image
from random import randint
from time import time

#settings for the random shift of the image
shiftfreq = 1200
maxshiftamount = 75
minshiftamount = 25



# Open the image
im = Image.open("Python\Tests\Images\Image.jpg")
returnedimage = Image.new("RGB", (im.size[0], im.size[1]), "white")

# Get the size of the image
width, height = im.size
print (f"Processing image of Width: {width}, Height: {height}")

randomshift = 0
time1 = time()



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
    # print(f"Row {x+1}/{height} processed with a shift of {randomshift}/{randomshiftdir}")

# Print the time taken
time2 = time()
print (f"Time taken: {(time2-time1)/60} Minutes")

# Save the image
print ("Saving image")
returnedimage.save("Python\Tests\Images\Initialtest.png")
print ("Image saved")

## show the image
image = Image.open("Python\Tests\Images\Initialtest.png")
image.show()