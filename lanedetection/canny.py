#!/usr/bin/env python3

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def findedge(img=None):
  img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  img = cv.bilateralFilter(img,9,75,75)
  img = cv.Canny(img, 100, 100)
  return img

def roi(img=None):
  # create black image
  mask2 = np.zeros(img.shape )
  print(mask2.shape)
  #fill poly 
  mask = cv.fillPoly(mask2, np.array([[(100,50), (400,50), (100,350), (400, 350)]]), 255)
  return mask
  



if __name__ == "__main__":

  img = cv.imread("sodukuCV.jpeg")
  img2 = img.copy()
  lines_img = findedge(img)
  interest = roi(lines_img)
  #print(img[:,:])
  plt.imshow(interest)
  plt.show()
  
  k = cv.waitKey(0)
  if k == ord("q"):         # wait for ESC key to exit
    cv.destroyAllWindows()
