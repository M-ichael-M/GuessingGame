#This script prepare image from UI layer to use in Guess Model

import PIL.Image as Image
import Constants

def property(im):
    cropIm = crop(im)
    toSquareIm = toSquare(cropIm)
    toArrayAndBinaryIm = toArrayAndBinary(toSquareIm)
    return toArrayAndBinaryIm
def crop(im):
    pass

def toSquare(beforeImg):
    image = Image.open(beforeImg)
    new_width = Constants.width
    new_height = Constants.height
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image

def toArrayAndBinary(beforeImg):
    w = 0
    h = 0
    listPx = []
    for i in range(Constants.width * Constants.height - 1):
        coordinate = w, h
        value = beforeImg.getpixel(coordinate)
        if value[0]+value[1]+value[2] >= 382:
            listPx.append(0)
        else:
            listPx.append(1)

        if w < Constants.width - 1:
            w = w + 1
        else:
            w = 0
            h = h + 1
    return listPx