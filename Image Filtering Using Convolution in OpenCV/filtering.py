import cv2
import numpy as np
 
image = cv2.imread('wood.jpg')

# Applying identity kernel to an image
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
 
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
 
cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
     
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()
 
# Blurring an image using custom 2D-cnvolutional kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)
     
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()

# Blurring an image using OpenCV's built-in function
img_blur = cv2.blur(src=image, ksize=(5,5)) 

cv2.imshow('Original', image)
cv2.imshow('Blurred', img_blur)
 
cv2.waitKey()
cv2.imwrite('blur.jpg', img_blur)
cv2.destroyAllWindows()

# Aplying Gaussian Blurring to an image
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)
 
cv2.imshow('Original', image)
cv2.imshow('Gaussian Blurred', gaussian_blur)
     
cv2.waitKey()
cv2.imwrite('gaussian_blur.jpg', gaussian_blur)
cv2.destroyAllWindows()

# Applying median blurring to an image
median = cv2.medianBlur(src=image, ksize=5)
 
cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median)
     
cv2.waitKey()
cv2.imwrite('median_blur.jpg', median)
cv2.destroyAllWindows()

# Sharpening an image using custom 2D-convolution kernels
kernel3 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
sharpen_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)
 
cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharpen_img)
     
cv2.waitKey()
cv2.imwrite('sharpen_image.jpg', sharpen_img)
cv2.destroyAllWindows()

# Applying bilateral filtering to an image
bilateral_filter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)
 
cv2.imshow('Original', image)
cv2.imshow('Bilateral Filtering', bilateral_filter)
 
cv2.waitKey(0)
cv2.imwrite('bilateral_filtering.jpg', bilateral_filter)
cv2.destroyAllWindows()