#!/usr/bin/env python3
import time
import cv2 as cv
from display import Display
import numpy as np

W = int(1920/2)
H = int(1080/2)

disp = Display(W, H)

class FeatureExtractor(object):
    GX = 16
    GY = 12

    def __init__(self):
        self.orb = cv.ORB_create()

    def extract(self, img):
        features = cv.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.015, minDistance=3)
        return features

fe = FeatureExtractor();


def processFrame(img):
    img = cv.resize(img, (W,H))
    kp = fe.extract(img)

    for f in kp:
        print(f)
        u,v = map(lambda x: int(round(x)), f[0])
        cv.circle(img, (u,v), color=(0,255,0), radius=3)
        
    disp.paint(img)

if __name__ == "__main__":
    cap = cv.VideoCapture("/home/neo/Code/PythonStuff/SLAM/testVid.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            processFrame(frame)
        else:
            break
