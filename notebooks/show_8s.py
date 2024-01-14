import sys

import cv2
from ultralytics import YOLO


if len(sys.argv) != 3:
    print("Использование: python show.py путь_до_модели путь_до_файла")
    sys.exit(1)

model_path = sys.argv[1]
file_path = sys.argv[2]

model = YOLO(model_path)

cap = cv2.VideoCapture(file_path)
while cap.isOpened():
    ret, frame = cap.read()

    results = model(frame, conf=0.55)[0].plot()

    cv2.imshow('YOLO', results)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
