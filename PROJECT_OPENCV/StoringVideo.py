import cv2

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size: {0} x {1}".format(width, height))

#웹캡영상 저장-VideoWriter class 사용
#인스턴스 생성
#1. 영상 파일명 지정하기
#2. 영상 포맷 결정하기 - fourcc ID (four character code) 4바이트 비디오 코덱
#3. 프레임수 지정하기
#4. 영상 크기(프레임 너비와 높이 튜플형태로 지정하기) - get()으로 프레임 너비, 높이 가져옴

#저장-write(), 파일닫기 - release()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('test.avi',fourcc,24, (int(width),int(height))) #프레임수 24개

while cap.isOpened():
    success, frame = cap.read()
    if success:
        writer.write(frame) #프레임 저장
        cv2.imshow('Video Window', frame)

        if cv2.waitKey(1)&0xFF == ord('q'):
            #q 누르면 실행 종료됨.
            break
    else:
        break

cap.release()
writer.release()#저장종료
cv2.destroyAllWindows()