#!/usr/bin/env python3

import cv2
import numpy as np
import argparse

cap = cv2.VideoCapture('driveRoad.mp4')

low_threshold = 50
high_threshold = 150

"""
Bild mit den punkten des ORB Algorithmus zeichnen.

@param img hier ein image/video
@return img2
"""
def punkteZeichnen(img):
  
  #edge detect
  orb = cv2.ORB_create() #objekt
  grayGaussianBlur = cv2.GaussianBlur(img, (5,5), 0)
  edges = cv2.Canny(grayGaussianBlur, low_threshold, high_threshold)
  lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 15, None, 50, 20)
  
  #finden der punkte und zeichnen der Punkte
  if img is None:
    print("Kein Input vorhanden Fehler!")
  else:
    punkte = orb.detect(grayGaussianBlur, None)
    punkte, des = orb.compute(grayGaussianBlur, punkte)
    print(punkte.pop())
    return
    img2 = cv2.drawKeypoints(grayGaussianBlur, punkte, grayGaussianBlur, color = (0, 0xff, 0), flags=0)
    #print("type of img2 is: ", type(gray))
  return img2

while True:      
    frame = cap.read()
    video = punkteZeichnen(frame[1])
    cv2.imshow("FrameDetection", video)
    k = cv2.waitKey(1) & 0xff
    print(k)
    if k == ord("q"):
        break
  
cv2.destroyAllWindows()
cap.release()
dir(cap.release())
