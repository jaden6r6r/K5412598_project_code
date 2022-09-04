#Handle imports from other files
from ast import main
from photopackTools import PhotopackTools
from matplotlib import image
import faceBlur as face
import os
import sys, getopt

def mainRun(args):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(args,"hi:o:",["ifilepath=","ofilepath="])
    except getopt.GetoptError:
        print("orchestration.py -i <inputfilepath> -o <outputfilepath>")
        sys.exit(2)
    print(opts)
    
    for opt, arg in opts:
        if opt == '-h':
            print('orchestration.py -i <inputfilepath> -o <outputfilepath>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        

    # return

    ##Deconstruct a .pdf to drive 
    photoTools = PhotopackTools()
    photoTools.deconstruct(inputfile)

    ###Pass deconstructed images through scanner 

    folder_dir = "./img/"
    for images in os.listdir(folder_dir):
        if (images.endswith(".png")):
            face.imgDetect('./img/{}'.format(images),images.replace('.png',''))

    ###Once scanned reconstruct using output images.
    photoTools.construct(inputfile,outputfile)


if __name__ == '__main__':
    mainRun(sys.argv[1:])
    