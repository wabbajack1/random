#!/usr/bin/env python3

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(np.complex.__dir__)


img = mpimg.imread("/Users/KerimErekmen/Desktop/test2.png")

print(img.shape)

region_of_interest_vertices = [
    (0, img.shape[0]),
    (img.shape[1] / 2, img.shape[0] / 2),
    (img.shape[1], img.shape[0]),
]


def region_of_interest(img, vertices):
    # Define a blank matrix that matches the image height/width.
    mask = np.zeros_like(img)
    # Retrieve the number of color channels of the image.
    channel_count = img.shape[2]
    # Create a match color with the same color channel counts.
    match_mask_color = (255,) * channel_count

    # Fill inside the polygon
    cv.fillPoly(mask, vertices, match_mask_color)

    # Returning the image only where mask pixels match
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(
    img,
    np.array([region_of_interest_vertices], np.int32),
)


plt.figure()
plt.imshow(cropped_image)
plt.show()
