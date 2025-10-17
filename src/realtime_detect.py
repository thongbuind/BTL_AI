import cv2
import json
from pathlib import Path
from ultralytics import YOLO
from utils import draw_status_box

import cv2

model = YOLO("/Users/thongbui.nd/Documents/Thong Bui/BTL_AI/model/best.pt")

current_file = Path(__file__).resolve()
project_root = current_file.parent.parent
config_file = project_root / "config.json"
src_dir = project_root / "src"

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("❌ Không mở được camera!")
    exit()

with open(config_file, 'r') as f:
    config = json.load(f)
image_size = config["image_size"]

while True:
    ret, frame = cam.read()
    if not ret:
        break

    results = model(frame, stream=True, imgsz=image_size, conf=0.75)

    detected_classes = set()
    for r in results:
        boxes = r.boxes
        for cls in boxes.cls:
            class_name = model.names[int(cls)]
            detected_classes.add(class_name)
        annotated_frame = r.plot()

    annotated_frame = draw_status_box(annotated_frame, detected_classes)

    cv2.imshow("YOLOv8 Real-time Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
