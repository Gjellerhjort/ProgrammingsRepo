from typing import Literal, Sequence
import cv2
from detectors.yolo_detector import YOLODetector
from detectors.generic_torch_detector import SSDDetector, FasterRCNNDetector
import os
from gui.app import *

MODEL_PATH = "models/"
IMAGE_PATH = "data/images/"
VIDEO_PATH = "data/video/"
DEVICE = "gpu"
CONF_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4

WINDOW_NAME = "video detection"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

DETECTOR_CLASSES = {
    "yolo": YOLODetector,
    "fasterrcnn": FasterRCNNDetector,
    "ssd": SSDDetector,
}

def run_on_image(detector, image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found!")
        return
    detector.detect(image)
    annotated = detector.annotate_frame(image)
    cv2.imshow("YOLO Image", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def run_on_video(detector, video_path):
    print(f"Using video: {video_path}")
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detector.detect(frame)
        annotated = detector.annotate_frame(frame)
        cv2.imshow(WINDOW_NAME, annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def choose_from_dir(dir_path: str, file_type: str, file_extensions: tuple[str, ...]) -> str:
    files = [f for f in os.listdir(dir_path) if f.lower().endswith(file_extensions)]
    print(f"Choose {file_type} file:")
    for i,v in enumerate(files):
        print(f"{i+1}: {v}")

    file_choice = int(input("Enter number: ")) -1
    if 0 <= file_choice < len(files):
        selected_file = files[file_choice]
        print(f"You chose: {selected_file}")
        return dir_path+selected_file
    else:
        print("Invalid choice")
        return ""

def choose_video_from_dir(video_path: str) -> str:
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.webm')
    return choose_from_dir(video_path, "video", video_extensions)
    
def choose_model_from_dir(model_path: str) -> str:
    model_extensions = (".onnx", ".pt")
    return choose_from_dir(model_path, "model", model_extensions) 

def choose_detectors():
    print("Choose detectors (comma-separated numbers, e.g. 1,2):")
    for i, det_name in enumerate(DETECTOR_CLASSES.keys()):
        print(f"{i+1}: {det_name}")
    choices = input("Enter numbers: ")
    selected = []
    keys = list(DETECTOR_CLASSES.keys())
    for ch in choices.split(","):
        idx = int(ch.strip()) - 1
        if 0 <= idx < len(keys):
            selected.append(keys[idx])
    return selected

def setup_detectors(detector_names, model_path):
    detectors = []
    for name in detector_names:
        DetectorClass = DETECTOR_CLASSES[name]
        if name == "yolo":
            chosen_model = choose_model_from_dir(model_path)
            detector = DetectorClass(chosen_model)
        else:
            detector = DetectorClass()
        detector.load_model()
        detectors.append(detector)
    return detectors

def main():
    detector_names = choose_detectors()
    if not detector_names:
        print("No detectors chosen, exiting.")
        return
    detectors = setup_detectors(detector_names, MODEL_PATH)
    video_path = choose_video_from_dir(VIDEO_PATH)
    if not video_path:
        print("No video chosen, exiting.")
        return
    # Launch the GUI app with detectors and video path
    launch_app(detectors, video_path)

if __name__ == "__main__":
    main()
