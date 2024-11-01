import cv2

video_capture = cv2.VideoCapture('Car.mp4')

if (video_capture.isOpened() == False):
    print("Error opening the video file")
else:
    fps = video_capture.get(5)
    print('Frames per second: ', fps, 'FPS')
    
    frame_count = video_capture.get(7)
    print('Frame count: ', frame_count)
    
while (video_capture.isOpened()):
    ret, frame = video_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        
        key = cv2.waitKey(270)
        
        if key == ord('q'):
            break
        else:
            break
        
video_capture.release()
cv2.destroyAllWindows()