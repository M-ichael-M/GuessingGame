#This script prepare image from UI layer to use in Guess Model
import Constants
import numpy as np
import cv2

global ImWidth
global ImHeight
global first_non_white_row
global first_non_white_col
global last_non_white_row
global last_non_white_col
def property(im):
    cropIm = crop(im)
    toSquareIm = toSquare(cropIm)
    toArrayAndBinaryIm = toArrayAndBinary(toSquareIm)
    return toArrayAndBinaryIm
def crop(im):
    global first_non_white_row
    global first_non_white_col
    global last_non_white_row
    global last_non_white_col
    non_white_pixels = np.any(im != 255, axis=2)
    first_row = np.argmax(non_white_pixels, axis=0)
    last_row = im.shape[0] - np.argmax(np.flipud(non_white_pixels), axis=0) - 1
    first_col = np.argmax(non_white_pixels, axis=1)
    last_col = im.shape[1] - np.argmax(np.flipud(non_white_pixels), axis=1) - 1

    first_non_white_row = int(first_row[first_row > 0][0])
    first_non_white_col = int(first_col[first_col > 0][0])
    last_non_white_row = int(last_row[last_row < im.shape[0] - 1][0])
    last_non_white_col = int(last_col[last_col < im.shape[1] - 1][0])

    ImHeight = last_non_white_col - first_non_white_col
    ImWidth = last_non_white_row - first_non_white_row

    if ImHeight<ImWidth:
        solve = 0
        if (ImWidth-ImHeight)%2 != 0:
            last_non_white_row+=1
        if ImWidth-ImHeight != 0:
            ImHeight = last_non_white_row - first_non_white_row
            solve = ImWidth-ImHeight/2
            last_non_white_row+=solve
            first_non_white_row-=solve
    if ImHeight>ImWidth:
        solve = 0
        if (ImHeight-ImWidth)%2 != 0:
            last_non_white_col+=1
        if ImHeight-ImWidth != 0:
            ImWidth = last_non_white_col - first_non_white_col
            solve = ImHeight-ImWidth/2
            last_non_white_col+=solve
            first_non_white_col-=solve



    first_non_white_row = int(first_non_white_row)
    first_non_white_col = int(first_non_white_col)
    last_non_white_row = int(last_non_white_row)
    last_non_white_col = int(last_non_white_col)

    cropArray = im[
        first_non_white_row: last_non_white_row + 1,
        first_non_white_col: last_non_white_col + 1,
        :
    ]
    return cropArray

def toSquare(beforeImg):
    newSide = Constants.width
    """ImWidth = last_non_white_row - first_non_white_row
    JumpRate = math.ceil(ImWidth/newSide)
    nwd = math.gcd(newSide, ImWidth)
    segmentImWidth = ImWidth/nwd
    segmentNewSide = newSide/nwd"""#Here will be resized method by me
    resized_image = cv2.resize(beforeImg, (newSide, newSide), interpolation=cv2.INTER_AREA)
    return resized_image

def toArrayAndBinary(beforeImg):
    w = 0
    h = 0
    listPx = []
    for i in range(Constants.width * Constants.height):
        coordinate = w, h
        value = np.array(beforeImg[w,h, :], dtype=np.uint16)
        if np.sum(value) >= 382:
            listPx.append(1)
        else:
            listPx.append(0)

        if w < Constants.width - 1:
            w = w + 1
        else:
            w = 0
            h = h + 1
    return listPx