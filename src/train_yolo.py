import json
from pathlib import Path
from ultralytics import YOLO

PROJECT_DIR = "/content/drive/MyDrive/BTL_AI"
DATASET_DIR = f"{PROJECT_DIR}/dataset"

try:
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent
except NameError:
    project_root = Path(PROJECT_DIR)

config_file = project_root / "config.json"
src_dir = project_root / "src"

with open(config_file, 'r') as f:
    config = json.load(f)
image_size = config["image_size"]
batch = config["batch"]
epochs = config["epochs"]

model = YOLO("yolov8n.pt")
model.train(
    data = f"{DATASET_DIR}/data.yaml",
    epochs = epochs,
    imgsz = image_size,
    batch = batch,
    device = 0,
    project=f"{PROJECT_DIR}/runs",
    name="RB19_detect",
)

print("Training xong! Kết quả lưu tại: runs/detect/train")
