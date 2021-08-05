import cv2
cap = cv2.VideoCapture(0)

#load classifiers
face_classifier = cv2.CascadeClassifier('.\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
lefteye_classifier = cv2.CascadeClassifier('.\opencv-master\data\haarcascades\haarcascade_lefteye_2splits.xml')
righteye_classifier = cv2.CascadeClassifier( '.\opencv-master\data\haarcascades\haarcascade_righteye_2splits.xml')
mouth_classifier = cv2.CascadeClassifier('.\opencv-master\data\haarcascades\haarcascade_smile.xml')

# Grab the width and height of the input video
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("size: {0} x {1}".format(frame_width, frame_height))

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tracking result.avi',fourcc, 30.0, (int(frame_width),int(frame_height)))

while cap.isOpened():

    # 카메라 프레임 읽기
    success, frame = cap.read()
    if not success:
        break

    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.1, 6)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # Select the region of the face, both gray and RGB
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # Detect the left eye and draw a circle around it
        lefteye = lefteye_classifier.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in lefteye:
            cv2.circle(roi_color, ((ex + ex + ew) // 2, (ey + ey + eh) // 2), 10, (255, 255, 0), 1)

            # Detect the right eye and draw a cricle around it also
        righteye = righteye_classifier.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in righteye:
            cv2.circle(roi_color, ((ex + ex + ew) // 2, (ey + ey + eh) // 2), 10, (255, 0, 255), 1)

            # Detect smile and draw rectangle around it
        mouth = mouth_classifier.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in mouth:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)

        cv2.imshow('Camera Window', frame)
        # Save the new video
        out.write(frame)
        print("Recording now......")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Close all opened files and save them
cap.release()
out.release()
cv2.destroyAllWindows()
