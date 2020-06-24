import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

gray= cv2.imread("fall-01-cam0-rgb-001.png", 0)
depth= cv2.imread("fall-01-cam0-d-001.png", 0)
x,y = gray.shape
""" temp = np.ones((x,y))
img3d = np.ones((x,y,256))
img3d = img3d*255
#print(img3d.shape)
for i in range(x):
    for j in range(y):
        img3d[i][j][depth[i][j]] = gray[i][j]
"""


cv2.imshow('GRAY', gray)
cv2.imshow('DEPTH', depth)
cv2.waitKey()

fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")
for i in range(256):
    axis.scatter(img3d[:,:,i], marker=".")