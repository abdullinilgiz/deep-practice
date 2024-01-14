import os
from pathlib import Path

from ultralytics import YOLO

directory_name = Path(__file__).resolve().parent.parent
model_path = os.path.join(directory_name, 'models', '100e_yolo8s.pt')

model = YOLO(model_path)

results = model.val()
