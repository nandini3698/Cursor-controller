import cv2,time,numpy as np,random
from pynput.mouse import Controller,Button
ms=Controller()
cam=cv2.VideoCapture(0)
facDet=cv2.CascadeClassifier(r'C:/Users/DELL/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
b=0
while True:
    r,i=cam.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=facDet.detectMultiScale(gray,1.3,7)
    if(len(face)>0):
        b=random.randint(1000,10000)
        print("Your OTP is: ",b)
        break
    cv2.imshow('image',i)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        break
cv2.destroyAllWindows()

print("Enter your OTP: ")
c=int(input())
if(b==c):
    while True:
        r,i=cam.read()
        j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        k=i[:,:,1]
        l=i[:,:,2]
        h=cv2.subtract(l,j)
        h=cv2.multiply(h,4)
        g1=cv2.subtract(k,j)
        g1=cv2.multiply(g1,4)
        r,g1=cv2.threshold(g1,35,255,0)
        g=cv2.flip(g1,1)
        r,h=cv2.threshold(h,40,255,0)
        cont1=cv2.findContours(g,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt1=cont1[0]
        cont2=cv2.findContours(h,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt2=cont2[0]
        L1=len(cnt1)
        L2=len(cnt2)
        if(L1>0 and L2>0):
            c=[]
            d=[]
            for x in range(0,L1):
                a=cv2.contourArea(cnt1[x])
                c.append(a)
            for y in range(0,L2):
                b=cv2.contourArea(cnt2[y])
                d.append(b)
            mx1=max(c)
            mx2=max(d)
            ind1=c.index(mx1)
            ind2=d.index(mx2)       
            if(d[ind2]>(c[ind1]-1000) and d[ind2]<(c[ind1]+1000)):
                ms.click(Button.left,1)
                time.sleep(0.1)
                ms.click(Button.left,1)
                
            else:
                m=cv2.moments(cnt1[ind1])
                if(m['m00']!=0):
                    cx=int(m['m10']/m['m00'])
                    cy=int(m['m01']/m['m00'])
                    print('centroid',cx,cy)
                    ms.position=(cx*(1920/720),cy*(1080/540))
                    
        cv2.imshow('image',g)
        k=cv2.waitKey(5)
        if(k==ord('q')):
            break
    cv2.destroyAllWindows()
        
    
else:
    print("Incorrect OTP")

