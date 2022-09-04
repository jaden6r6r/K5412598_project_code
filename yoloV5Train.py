import os
import numpy as np
import matplotlib.pyplot as plt
from glob import glob as g
import cv2
from shutil import copy, move

def _val_dataset_reformat():
    #Configure the Val Dataset 
    new_imgs_dir = 'E:/content/newDataset/images/val'
    new_lbls_dir = 'E:/content/newDataset/labels/val'
    label_text_name = 'E:/wider_face_split/wider_face_val_bbx_gt.txt'
    imgs_address = 'E:/WIDER_val/images/'

    #Create the directories for the val images and labels
    os.makedirs(new_imgs_dir,exist_ok = True)
    os.makedirs(new_lbls_dir,exist_ok = True)

    #Open the txt file containing all the image names 
    annots = open(label_text_name) 
    lines = annots.readlines()
    names =   [x for x in lines if 'jpg' in x]
    indices = [lines.index(x) for x in names]
    print(len(names))
    #iterate for the length of the names array. 
    for n in range(len(names[:])):
        i = indices[n]
        name = lines[i].rstrip()
        old_img_path = os.path.join(imgs_address , name)
        name = name.split('/')[-1]
        label_path = os.path.join(new_lbls_dir , name.split('.')[0] + '.txt')
        img_path = os.path.join(new_imgs_dir , name)
        
        num_objs = int(lines[i+1].rstrip())
        bboxs = lines[i+2 : i+2+num_objs]
        bboxs = list(map(lambda x:x.rstrip() , bboxs))
        bboxs = list(map(lambda x:x.split()[:4], bboxs))
        print(old_img_path)
        # if len(bboxs) > 5:
        #     continue
        img = cv2.imread(old_img_path)
        print(img)
        img_h,img_w,_ = img.shape
        img_h,img_w,_ = img.shape
        f = open(label_path, 'w')
        count = 0 # Num of bounding box
        for bbx in bboxs:
            x1 = int(bbx[0])
            y1 = int(bbx[1])
            w = int(bbx[2])
            h = int(bbx[3])
        #     #yolo:
            x = (x1 + w//2) / img_w
            y = (y1 + h//2) / img_h
            w = w / img_w
            h = h / img_h
            if w * h * 100 > 2:
                yolo_line = f'{0} {x} {y} {w} {h}\n'
                f.write(yolo_line)
                count += 1
        f.close()
        if count > 0:   
            copy(old_img_path , img_path)
        else:
            os.remove(label_path)

def _train_dataset_reformat():
    #Configure the Val Dataset 
    new_imgs_dir = 'E:/content/newDataset/images/train'
    new_lbls_dir = 'E:/content/newDataset/labels/train'
    label_text_name = 'E:/wider_face_split/wider_face_train_bbx_gt.txt'
    imgs_address = 'E:/WIDER_train/images/'

    #Create the directories for the val images and labels
    os.makedirs(new_imgs_dir,exist_ok = True)
    os.makedirs(new_lbls_dir,exist_ok = True)

    #Open the txt file containing all the image names 
    annots = open(label_text_name) 
    lines = annots.readlines()
    names =   [x for x in lines if 'jpg' in x]
    indices = [lines.index(x) for x in names]
    print(len(names))
    #iterate for the length of the names array. 
    for n in range(len(names[:])):
        i = indices[n]
        name = lines[i].rstrip()
        old_img_path = os.path.join(imgs_address , name)
        name = name.split('/')[-1]
        label_path = os.path.join(new_lbls_dir , name.split('.')[0] + '.txt')
        img_path = os.path.join(new_imgs_dir , name)
        
        num_objs = int(lines[i+1].rstrip())
        bboxs = lines[i+2 : i+2+num_objs]
        bboxs = list(map(lambda x:x.rstrip() , bboxs))
        bboxs = list(map(lambda x:x.split()[:4], bboxs))
        print(old_img_path)
        # if len(bboxs) > 5:
        #     continue
        img = cv2.imread(old_img_path)
        print(img)
        img_h,img_w,_ = img.shape
        img_h,img_w,_ = img.shape
        f = open(label_path, 'w')
        count = 0 # Num of bounding box
        for bbx in bboxs:
            x1 = int(bbx[0])
            y1 = int(bbx[1])
            w = int(bbx[2])
            h = int(bbx[3])
        #     #yolo:
            x = (x1 + w//2) / img_w
            y = (y1 + h//2) / img_h
            w = w / img_w
            h = h / img_h
            if w * h * 100 > 2:
                yolo_line = f'{0} {x} {y} {w} {h}\n'
                f.write(yolo_line)
                count += 1
        f.close()
        if count > 0:   
            copy(old_img_path , img_path)
        else:
            os.remove(label_path)
def resize_img(input_name , output_name, target_width = 640):
    im = cv2.imread(input_name)
    h,w,_  = im.shape
    target_height = int(h / w * target_width)
    im = cv2.resize(im , (target_width , target_height), interpolation = cv2.INTER_AREA)
    cv2.imwrite(output_name , im)

def resize_all_imgs(imgs_dir):
    names = g(os.path.join(imgs_dir , '*'))
    for img in names:
        resize_img(img, img)

names = g('E:/content/newDataset/labels/*/*')
print(f'Threre are {len(names)}  images')
resize_all_imgs('E:/content/newDataset/images/*')

n = np.random.randint(0, len(names))
f = open(names[n])

lines = f.readlines()

n = np.random.randint(0, len(names))
f = open(names[n])

lines = f.readlines()
classes = list(map(lambda x: int(x[0]), lines))
lines = list(map(lambda x:x.rstrip()[2:], lines))
objects = list(map(lambda x:(x.split()), lines))

img = cv2.imread(names[n].replace('txt','jpg').replace('labels', 'images'))
for c, bbox in zip(classes, objects):
  bbox = list(map(lambda x:float(x), bbox))
  x,y,w,h = bbox
  img_h = img.shape[0]
  img_w = img.shape[1]
  x = int(x * img_w)
  w = int(w * img_w)
  y = int(y * img_h)
  h = int(h * img_h)
  color = (255,100,50)
  cv2.rectangle(img , (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), color , 4)
plt.figure(figsize = (8,8))
plt.imshow(img[:,:,::-1]); plt.axis('off')
print(f'number of bounding boxes : {len(classes)}')
print(f'Shape on the image : {img.shape}')

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

images = []
for _ in range(25):
    n = np.random.randint(0, len(names))
    f = open(names[n])

    lines = f.readlines()
    classes = list(map(lambda x: int(x[0]), lines))
    lines = list(map(lambda x:x.rstrip()[2:], lines))
    objects = list(map(lambda x:(x.split()), lines))

    img = cv2.imread(names[n].replace('txt','jpg').replace('labels', 'images'))
    for c, bbox in zip(classes, objects):
        bbox = list(map(lambda x:float(x), bbox))
        x,y,w,h = bbox
        img_h = img.shape[0]
        img_w = img.shape[1]
        x = int(x * img_w)
        w = int(w * img_w)
        y = int(y * img_h)
        h = int(h * img_h)
        color = (255,100,50)
        cv2.rectangle(img , (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), color , 6)
    # plt.figure(figsize = (8,8))
    # plt.imshow(img[:,:,::-1]); plt.axis('off')
    # print(f'number of bounding boxes : {len(classes)}')
    images.append(img[:,:,::-1])
fig = plt.figure(figsize=(16., 16.))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(5 ,5),  # creates 2x2 grid of axes
                 axes_pad=0.1,  # pad between axes in inch.
                 )

for ax, im in zip(grid, images):
    # Iterating over the grid returns the Axes.
    ax.imshow(im)
    ax.axis('off')

plt.show()