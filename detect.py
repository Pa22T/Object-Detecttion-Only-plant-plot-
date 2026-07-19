from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # nano model
results = model("test.jpg")