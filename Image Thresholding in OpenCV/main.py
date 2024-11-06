import cv2
src = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", src)
cv2.waitKey(0)

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY)
cv2.imwrite("opencv-threshold-example.png", dst)
cv2.imshow("THRESH BINARY", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Thresholding with maxValue set to 128
th, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY)
cv2.imwrite("opencv-thresh-binary-maxval.png", dst)
cv2.imshow("THRESH BINARY with max value 128", dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 
 
# Thresholding with threshold value set 127 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY) 
cv2.imwrite("opencv-thresh-binary.png", dst)
cv2.imshow("THRESH BINARY with threshld 127", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Thresholding using THRESH_BINARY_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY_INV) 
cv2.imwrite("opencv-thresh-binary-inv.png", dst)
cv2.imshow("THRESH BINARY IVERSE", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Thresholding using THRESH_TRUNC 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC) 
cv2.imwrite("opencv-thresh-trunc.png", dst)
cv2.imshow("THRESH TRUNC", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Thresholding using THRESH_TOZERO 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO)
cv2.imwrite("opencv-thresh-tozero.png", dst)
cv2.imshow("THRESH TOZERO", dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 
 
# Thresholding using THRESH_TOZERO_INV 
th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV)
cv2.imwrite("opencv-thresh-to-zero-inv.png", dst)
cv2.imshow("THRESH TOZERO INVERSE", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()