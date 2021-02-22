# -*- coding: utf-8 -*-
"""
Created on Wed Jan 09 11:20:52 2019

@author: pmoran
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("board.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (7, 7), 0)
edges = cv2.Canny(gray,50,250,apertureSize = 3)

#Plot the original image side-by-side with the edge image
plt.figure(1)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

lines = cv2.HoughLines(edges,1,np.pi/180,200)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

rho, theta = zip(*lines[0])
theta = np.rad2deg(theta)

plt.figure(2)
plt.plot(rho,theta, 'ro')
plt.title('Hough Space'), plt.xticks([]), plt.yticks([])
plt.xlabel('Distance (pixels)')
plt.ylabel('Orientation (theta)')


cv2.imwrite('houghlines.jpg',img)