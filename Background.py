# Background-construction

import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
os.getcwd()
os.chdir("C:\Users\gaurav.hegde\Documents\Python Scripts")
os.getcwd()

vidcap = cv2.VideoCapture('store1.mp4')
#vidcap.set(0,20000)
ret,image = vidcap.read()
pixel_blue=[]
pixel_green=[]
pixel_red=[]
blue=0
red=0
green=0
frame=0
image_final=image.copy()
image_final.fill(255)
#cv2.imshow('image',image_final)
#cv2.waitKey(0)
###################### sabarna ###############
height, width = image.shape[:2]
for i in range(0,height):
    for j in range(1,width):
        vidcap = cv2.VideoCapture('store1.mp4')
        ret,image = vidcap.read()
        frame=0
        while ret and frame%1000==0:
            #print "top",frame
            ret,image = vidcap.read()
            vidcap.set(0, frame)
            if ret :
                pixel_blue.append(image[i,j,0])
                pixel_green.append(image[i,j,1])
                pixel_red.append(image[i,j,2])
            frame+=1
            print "in",frame
        blue=int(stats.mode(pixel_blue)[0][0])
        green=int(stats.mode(pixel_green)[0][0])
        red=int(stats.mode(pixel_red)[0][0])
        
        image_final[i,j,0]=blue
        image_final[i,j,1]=green
        image_final[i,j,2]=red
        
        pixel_blue=[]
        pixel_green=[]
        pixel_red=[]
        print i,j
        
cv2.imwrite("final_background.png",image_final)
