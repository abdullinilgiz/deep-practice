import os
from pathlib import Path

from ultralytics import YOLO


directory_name = Path(__file__).resolve().parent.parent
dataset_yaml_path = os.path.join(directory_name, 'notebooks', 'datasetv8.yaml')

model = YOLO('yolov8s.pt')

results = model.train(
    data=dataset_yaml_path,
    epochs=100,
    imgsz=960,
    batch=4
    )

results = model.val()
