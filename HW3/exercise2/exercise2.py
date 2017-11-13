import cv2

image = cv2.imread('Lenna.png')
cv2.imshow('img',image)

b,g,r = cv2.split(image)
cv2.imshow('rgbb',b) #blue channel
cv2.imshow('rgbg',g) #green channel
cv2.imshow('rgbr',r) #red channel

cv2.imwrite('blue channel.png',b) #save b
cv2.imwrite('green channel.png',g) #save g
cv2.imwrite('red channel.png',r) #save r

pixel = image[20.25]
print('BGR=', pixel)

ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y,cb,cr = cv2.split(ycbcr)
cv2.imshow('y',y) #show y
cv2.imshow('cb',cb) # show cb
cv2.imshow('cr', cr) # show cr

cv2.imwrite('y.jpg',y) # save y
cv2.imwrite('cb.jpg',Cb) #save cb
cv2.imwrite('cr.jpg',Cr) #save cr

pixel= img[20, 25]
print ('ycbcr=',pixel)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert to hsv
h,s,v = cv2.split(hsv)
cv2.imshow('Hue',h) #show hue
cv2.imshow('Saturation',s) #show saturation
cv2.imshow('Value',v) #show value
cv2.imwrite('Saturation.jpg',s) #save saturation
cv2.imwrite('Hue.jpg',h) #save hue
cv2.imwrite('Value.jpg',v) #save value

pixel= img[20, 25]
print ('hsv=',pixel)

cv2.waitKey(0)
cv2.destroyAllWindows()
