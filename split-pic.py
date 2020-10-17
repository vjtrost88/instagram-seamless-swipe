#!/usr/bin/venv python

from PIL import Image
import argparse
import os, sys

def getArgs():
    parser = argparse.ArgumentParser(description='Split a landscape picture into k vertical slices.')
    parser.add_argument('-p', '--path', help="path to the image we're splitting", required=True)
    parser.add_argument('-k', '--k', help="number of slices to do", required=True)

    args = parser.parse_args()
    path = args.path
    k = args.k

    return path, k


def main():
    '''
        Split a picture into k slices for seamless swipe on insta
        Input a picture
        Send params about the following:
            path: path to image file we're splitting
            k: number of slices to do
            aspect-ratio: the aspect ratio for the slices you want (5x4 or 16x9)
        It will automatically save the slices to ./slices
        NOTE: you need to input a picture ahead of time that will slice into the right aspect aspect_ratio
              so like 8x5 for 2 4x5's or 27x16 for 3 9x16's
    '''
    path, k = getArgs()


    #get the file name
    shit = path.split('/')
    filename = shit[len(shit)-1].split(".")[0]

    # get the out path
    shit = shit[:-1]
    outpath = os.path.join(*shit)
    outpath = '/' + outpath

    # read in the landscape image
    im = Image.open(path)
    print("We want {} slices from image with dims {}".format(k, im.size))
    #sys.exit()


    # if the slices folder does not exist, create it
    if not os.path.exists(outpath + '/' + 'slices'):
        os.makedirs(outpath + '/' +'slices')

    # for each slice, crop based on a dimesnion-based schema,
    # iteratively defining the slice by multiplying the width
    # by a factor of k
    k = int(k)
    h = im.size[1]
    w = im.size[0]

    # format for im.crop is (left, top, right, bottom)
    for j in range(0, k):
        left = (w/k)*j
        top = 0
        right = (w/k)*(j+1)
        bottom = h

        slice = (left, top, right, bottom)
        print(slice)
        a = im.crop(slice)
        out = os.path.join(outpath, "slices", filename)
        out = out + '-{}.{}'.format(str(j), "jpg")
        print(out)
        a.save(out, quality=100)


if __name__ == '__main__':
    main()
