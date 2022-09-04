import os
import time

import cv2
import torch
from PIL import Image


def imgDetect(imgPath: str, imgName: str):

    model = torch.hub.load(
        'ultralytics/yolov5',
        'custom',
        path='./yolov5/runs/train/yolo_reg_det_05_01_150_epochs3/weights/best.pt',
    )
    model.conf = 0.05

    # batch of images
    imgs = cv2.imread(imgPath)

    y, x = imgs.shape[0], imgs.shape[1]
    imgs = imgs[0 : y - 9, 0:x]

    # DEBUG
    # print(x, y)
    
    results = model(imgs, size=640)  # includes NMS
    print(results)
    for x in range(len(results.xyxy[0])):
        x1 = int(results.xyxy[0][x][0])
        y1 = int(results.xyxy[0][x][1])
        x2 = int(results.xyxy[0][x][2])
        y2 = int(results.xyxy[0][x][3])

        #DEBUG print('bounding box is ', x1, y1, x2, y2)

        # # Create ROI coordinates
        topLeft = (x1, y1)
        bottomRight = (x2, y2)
        x, y = topLeft[0], topLeft[1]
        w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

        # # Grab ROI with Numpy slicing and blur
        ROI = imgs[y : y + h, x : x + w]
        blur = cv2.GaussianBlur(ROI, (51, 51), 0)

        # Insert ROI back into image
        imgs[y : y + h, x : x + w] = blur

    # cv2.imshow('blur', blur)
    # if len(results.xyxy[0]) > 0:
    #     # cv2.imshow('image', imgs)
    #     cv2.waitKey()
    #     dir_part = "./img/complete/"
    #     cv2.imwrite('{}.png'.format(dir_part + str(imgName)  + "_edit"), imgs)
    #     return 1

    cv2.waitKey()
    dir_part = "./img/complete/"
    cv2.imwrite('{}_edit.png'.format(dir_part + str(imgName)), imgs)
    return 1


if __name__ == '__main__':
    import glob
    imgDetect("C:/temp/face1.jpg","face1")


