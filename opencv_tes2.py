import numpy
import cv2
from PIL import Image, ImageDraw

# read image as RGB (without alpha)
img = Image.open("output.jpg").convert("RGB")

# convert to numpy (for convenience)
img_array = numpy.asarray(img)

# create mask
polygon = [(481,26),(350,50),(240,123),(150,4),(400,324)]

# create new image ("1-bit pixels, black and white", (width, height), "default color")
mask_img = Image.new('1', (img_array.shape[1], img_array.shape[0]), 0)

ImageDraw.Draw(mask_img).polygon(polygon, outline=1, fill=1)
mask = numpy.array(mask_img)


# assemble new image (uint8: 0-255)
new_img_array = numpy.empty(img_array.shape, dtype='uint8')

# copy color values (RGB)
new_img_array[:,:,:3] = img_array[:,:,:3]

# filtering image by mask
new_img_array[:,:,0] = new_img_array[:,:,0] * mask
new_img_array[:,:,1] = new_img_array[:,:,1] * mask
new_img_array[:,:,2] = new_img_array[:,:,2] * mask

# font
font = cv2.FONT_HERSHEY_SIMPLEX
# fontScale
fontScale = 0.3
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 1

# back to Image from numpy
newIm = Image.fromarray(new_img_array, "RGB")
newIm.save("out.jpg")
image = cv2.imread('out.jpg')
img_dimen = image.shape
for value in polygon:
    # org
    print (value)
    #you can't change the value of tuple so we change it to a list here
    org = list(value)
    if value[1] < 10 or value[1] > img_dimen[1] - 10:  # looking for the y of pint is near the end of the img
        print("safe zone")
        if value[1] < 10:
            org[1] = org[1]+10 #why do you want to do this            to be able in automatic to see al the text alse if is near the border



    text='p: %s'% str(value)

    # Using cv2.putText() method
    #puttext method wont take a list so we change it back to tuple
    org = tuple(org)
    image = cv2.putText(image, text , org, font,fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('Image', image)
cv2.waitKey(0)

