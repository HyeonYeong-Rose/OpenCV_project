import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    (x, y, w, h) = cv2.boundingRect(cnt)
    roi = frame[y:y + h, x:x + w] #frame리스트 안에서 x좌표를 여기서 저기까지, y좌표를 여기서 저기까지

    rows, cols, _ = roi.shape

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) #의미없는 색상 데이터 제거해서 데이터량 줄이기
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

    _, threshold = cv2.threshold(gray_roi, 5, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        #(x,y,w,h) =cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.line(roi, (x+int(w/2),0), (x+int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2), (cols, y + int(h / 2)), (0, 255, 0), 2)
        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)

        break


    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)


   #cv2.imshow("Frame", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()