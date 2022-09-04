import glob
import os
import pathlib
import re
import sys
import time

import cv2
import dlib
import numpy as np


class FaceScanner:
    def __init__(self):
        self.detected = []
        # self.scanned_img = f"{pathlib.Path(__file__).parent.parent.resolve()}/complete/"

    def _get_photo_dir(self):
        pass

    def face_scanner(self, image):
        start = time.time()
        detected = []

        img = dlib.load_rgb_image(image)
        img_2 = img.copy()

        face_detector = dlib.cnn_face_detection_model_v1("dlib\\mmod_human_face_detector.dat")
        try:
            dets = face_detector(img, 1)
        except Exception as e:
            print(e)

        print("Number of faces detected: {}".format(len(dets)))
        for i, d in enumerate(dets):
            # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            #    i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), d.confidence))

            left = d.rect.left()
            top = d.rect.top()
            right = d.rect.right()
            bottom = d.rect.bottom()

            cv2.rectangle(img, (left, top), (right, bottom), (124, 34, 0), 2)

            h = d.rect.height()
            w = d.rect.width()
            # top point through to top point plus height, left point through to left point plus width
            if len(img[top : top + h, left : left + w]) == 0:
                continue
            else:
                sub_face_images = img[top : top + h, left : left + w]
                blurred_faces = cv2.GaussianBlur(sub_face_images, (103, 103), 50)
                img_2[
                    top : top + sub_face_images.shape[0],
                    left : left + sub_face_images.shape[1],
                ] = blurred_faces

                blurred_image_filename = (
                    str(image[len(image) - 15 :]).replace("\\", "").replace(".jpg", "")
                )
                print('FACESCAN', blurred_image_filename)
                try:
                    cv2.imwrite(
                        str(f"{self.scanned_img}{blurred_image_filename}-face.jpg"),
                        cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB),
                    )
                except:
                    print("Error writing image")

                return 1
                
        end = time.time()
        print(end - start)

        return None


if __name__ == '__main__':
    a = FaceScanner()
