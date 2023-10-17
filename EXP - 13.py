import cv2
import numpy as np
video_capture=cv2.VideoCapture('VID6.mp4')
if not video_capture.isOpened():
    print("Error can't open file")
    exit()
original_points=np.float32([[56, 65], [100,24], [28, 320], [156, 390]])
transformed_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
perspective_matrix=cv2.getPerspectiveTransform(original_points,transformed_points)
while True:
    ret,frame=video_capture.read()
    if not ret:
        break
    
    perspective_video=cv2.warpPerspective(frame,perspective_matrix,(1000,1000))
    cv2.imshow('Perspective Transformed Video',perspective_video )
    if cv2.waitKey(1)&0*FF==27:
        break
video_capture.release()
cv2.destroyAllWindows()
