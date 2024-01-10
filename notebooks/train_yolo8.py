from ultralytics import YOLO

model = YOLO('yolov8s.pt')

results = model.train(
    data='notebooks/datasetv8.yaml',
    epochs=100,
    imgsz=960,
    batch=4
    )

results = model.val()
