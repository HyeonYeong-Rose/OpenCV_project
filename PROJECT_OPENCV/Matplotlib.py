#읽어들인 이미지 보여주기
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test_retriever.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()