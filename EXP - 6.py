import cv2

# Open the video file
video_capture = cv2.VideoCapture('VID6.mp4')

if not video_capture.isOpened():
    print("Error: Couldn't open the video file")
    exit()

while True:
    ret, frame = video_capture.read()
    
    if not ret:
        break

# Slow motion (play at half the speed)
    cv2.imshow('Slow Motion Video', frame)
    if cv2.waitKey(50) & 0xFF == 27:  # 50 ms delay between frames (20 frames per second)
        break

# Fast motion (play at double the speed
    cv2.imshow('Fast Motion Video', frame)
    if cv2.waitKey(25) & 0xFF == 27:  # 25 ms delay between frames (40 frames per second)
        break

video_capture.release()
cv2.destroyAllWindows()
