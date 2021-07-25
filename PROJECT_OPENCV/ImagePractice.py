import cv2

print(cv2.__version__) #open cv 버전 확인

# 이미지 읽기
img = cv2.imread('test_cocatoo.png', 1) #해당프로젝트 폴더 안에 사진저장

# 이미지 화면에 표시
cv2.imshow('Test Lovely Cocatoo Image', img) #(윈도우 창제목, 전달받은 프레임넘버)
cv2.waitKey(0)

# 이미지 윈도우 삭제
cv2.destroyAllWindows()

# 이미지 다른 파일로 저장
cv2.imwrite('test_another_file.png', img) #다른이름으로 사진저장 성공.

