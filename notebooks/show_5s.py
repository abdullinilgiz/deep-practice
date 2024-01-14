import sys

import torch
import numpy as np
import cv2

if len(sys.argv) != 3:
    print("Использование: python show.py путь_до_модели путь_до_файла")
    sys.exit(1)

model_path = sys.argv[1]
file_path = sys.argv[2]

model = torch.hub.load('ultralytics/yolov5',
                       'custom',
                       path=model_path,
                       force_reload=True)

cap = cv2.VideoCapture(file_path)
while cap.isOpened():
    ret, frame = cap.read()

    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
