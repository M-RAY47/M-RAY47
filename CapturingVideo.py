import cv2


video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()
    print(frame)
    # convert each frame into a gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow("Capture", frame)
    key = cv2.waitKey(1)  # this generate a new frame every milliseconds
    if key == ord("q"):
        break
print(a)  # this will print the number of frames

video.release()
cv2.destroyAllWindows()
#   time.sleep(2000)
