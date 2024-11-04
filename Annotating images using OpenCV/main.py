import cv2

img = cv2.imread('sample.jpg')

cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if img is None:
    print('Image not found.')
    exit()

# DRawing a line
imageLine = img.copy()
pointA = (200, 80)
pointB = (450, 80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness = 3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)


# Drawing a circle
imageCircle = img.copy()
circle_center = (415,190)
radius =100
cv2.circle(imageCircle, circle_center, radius, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA) 
cv2.imshow("Image Circle",imageCircle)
cv2.waitKey(0)

# Drawing a filled circle
imageFilledCircle = img.copy() 
circle_center = (415,190)
radius =100
cv2.circle(imageFilledCircle, circle_center, radius, (255, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow('Image with Filled Circle',imageFilledCircle)
cv2.waitKey(0)

# Drawing a rectangle
imageRectangle = img.copy()
start_point =(300,115)
end_point =(475,225)
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(0)

# DRawing an ellipse
imageEllipse = img.copy()
ellipse_center = (415, 190)
axis1 = (100, 50)
axis2 = (125, 50)
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
cv2.imshow('ellipse image', imageEllipse)
cv2.waitKey(0)

# Drawing a half-ellipse
halfEllipse = img.copy()
ellipse_center = (415,190)
axis1 = (100,50)
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 180, 360, (255, 0, 0), thickness=3)
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 0, 180, (0, 0, 255), thickness=-2)
cv2.imshow('halfEllipse',halfEllipse)
cv2.waitKey(0)

# Adding text
imageText = img.copy()
text = 'I am a Happy dog!'
org = (50,350)
cv2.putText(imageText, text, org, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (250,225,100))
cv2.imshow("Image Text",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()