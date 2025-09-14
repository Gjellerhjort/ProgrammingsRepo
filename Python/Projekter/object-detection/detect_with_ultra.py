from ultralytics import YOLO

model = YOLO("models/yolo11n.pt")
results = model("data/images/group-people.jpg")


