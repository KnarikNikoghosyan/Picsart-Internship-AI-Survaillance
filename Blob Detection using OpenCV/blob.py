import cv2
import numpy as np
 
img = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
 
# Filter by Area
params.filterByArea = True
params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
 
# Creating detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
 
# Detecting blobs
keypoints = detector.detect(img)
 
# Drawing  detected blobs as red circles and ensuring the size of the circle corresponds to the size of blob
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
