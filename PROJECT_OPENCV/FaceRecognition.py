import cv2
import cvlib
from cvlib.object_detection import draw_bbox

cam = cv2.VideoCapture(0) #0: default camera
#실시간 웹캠화면 출력 성공

while cam.isOpened():
    status, frame = cam.read()

    bbox, label, conf = cvlib.detect_common_objects(frame)#물체 검출
    print(bbox, label, conf)

    line = draw_bbox(frame, bbox, label, conf, write_conf=True)

    cv2.imshow('Realtime object detection', line)

    key = cv2.waitKey(1) & 0xFF
    if (key == 27):# ESC를 누르면 종료
        break

cam.release()
cv2.destroyAllWindows()