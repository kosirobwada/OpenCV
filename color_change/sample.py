import cv2
import numpy as np
file_name='logo.png'
img=cv2.imread(file_name,cv2.IMREAD_COLOR)
img=cv2.resize(img,(1000,600))
def click_pos(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        img2=np.copy(img)
        cv2.circle(img2,center=(x,y),radius=5,color=(0,0,0),thickness=-1)
        B,G,R=img[y,x,:]
        bgr_str='(B,G,R)=('+str(B)+','+str(G)+','+str(R)+')'
        cv2.putText(img2,bgr_str,(30, 50),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2,cv2.LINE_AA)
        cv2.imshow('window', img2)
        
cv2.imshow('window', img)
cv2.setMouseCallback('window', click_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()