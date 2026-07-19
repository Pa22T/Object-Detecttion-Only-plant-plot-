from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train
train_results = model.train(
    data="datasets/data.yaml",
    epochs=100,
    imgsz=640,
    device=0,       # ถ้ามี GPU
    workers=0
)

# Validate
val_results = model.val(workers=0)