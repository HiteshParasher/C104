import cv2

img = cv2.imread("Sun.jpg")
rocket=img[120:360,400:500]
img[10:250,10:110]=rocket


cv2.putText(img,
            "Sun.jpg",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5
            (255,255,255)
)
            
             



cv2.imshow("Output",img)

cv2.waitKey(0)
