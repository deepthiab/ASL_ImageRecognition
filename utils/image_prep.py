from PIL import Image, ImageFilter
import numpy as np


def imageprepare(img):
    """
    This function returns a 28x28 pixel value matrix
    The input is an image
    """
    im = img.convert('L') #convert to gray scale
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 28 pixels.
        nheight = int(round((28.0 / width * height), 0))  # resize height according to ratio width
        if (nheight == 0):  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((28, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (0, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((28.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 28), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical position
        newImage.paste(img, (wleft, 0))  # paste resized image on white canvas

    x = list(newImage.getdata())  # get pixel values
    x = np.asarray(x) #convert to an array
    x = np.reshape(x,(1,28,28,1))
    x = x.astype('float32')/255
    
    return x


#Credits : https://stackoverflow.com/questions/35842274/convert-own-image-to-mnists-image