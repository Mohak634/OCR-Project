import easyocr
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_number=1
while os.path.isfile(f"OCR Samples/{image_number}.jpg"):
    try:
        IMAGE_PATH = f"OCR Samples/{image_number}.jpg"

        reader = easyocr.Reader(['en'])
        result = reader.readtext(IMAGE_PATH)
        print(result)

        top_left = tuple(result[0][0][0])
        bottom_right = tuple(result[0][0][2])
        text = result[0][1]
        font = cv2.FONT_HERSHEY_SIMPLEX

        img = cv2.imread(IMAGE_PATH)
        spacer = 100
        for detection in result:
            top_left = tuple(detection[0][0])
            bottom_right = tuple(detection[0][2])
            text = detection[1]
            img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
            img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
            spacer+=15

        plt.imshow(img)
        plt.show()
    finally:
        image_number+=1
        

