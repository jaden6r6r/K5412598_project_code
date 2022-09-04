#Handle imports from other files
from photopackTools import PhotopackTools
from matplotlib import image
import faceBlur as face
import os

##Deconstruct a .pdf to drive 
photoTools = PhotopackTools()
photoTools.deconstruct('./test_face.pdf')

###Pass deconstructed images through scanner 

folder_dir = "./img/"
for images in os.listdir(folder_dir):
    if (images.endswith(".png")):
        face.imgDetect('./img/{}'.format(images),images.replace('.png',''))

###Once scanned reconstruct using output images.
photoTools.construct('./output.pdf')

