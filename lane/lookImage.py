#!/usr/bin/env python3

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread("/Users/KerimErekmen/Desktop/test2.png")


region_of_interest_vertices = [
      (0, 700),
      (img.shape[1], img.shape[0] / 2),
      (1600, 1000),
  ]

mask = np.zeros_like(img)
match_mask_color = (255,) * img.shape[2] 

b = cv.fillPoly(np.zeros_like(img), list(np.array([region_of_interest_vertices], np.int32)), match_mask_color)

masked_image = cv.bitwise_and(mask, img)

for i in masked_image:
  print(i)

plt.figure()
plt.imshow(b)
plt.show()
