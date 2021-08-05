import cv2
import time

start = time.time()
cap = cv2.VideoCapture(0) #0: default camera
#실시간 웹캠화면 출력 성공

#cap = cv2.VideoCapture("Me_in_IKEA.mp4") #동영상 파일에서 읽기성공


faceCascade = cv2.CascadeClassifier(
    '.\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml'
   #'.\opencv-master\data\haarcascades\haarcascade_eye.xml'
)
while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if not success:
        break
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        # 프레임 출력
        cv2.imshow('Camera Window', frame)
        print('등장한 얼굴 개수',faces.shape[0])
        # ESC를 누르면 종료
        key = cv2.waitKey(1) & 0xFF
        if (key == 27):
            break


end = time.time()
cap.release()
cv2.destroyAllWindows()

print('소요시간', f"{end-start: .5f} sec")
