import numpy as np
from detectors.base_detector import BaseDetector
from ultralytics import YOLO

class YOLODetector(BaseDetector):
    def load_model(self):
        self.model = YOLO(self.model_path, task="detect")        

    def detect(self, image: np.ndarray):
        # Stub implementation. Replace with actual inference code.
        # Example output format:
        results = self.model.predict(image, classes=[0], verbose=False)
        # Convert results to the expected format.
        detections = []

        for result in results:
            for i, box in enumerate(result.boxes):
                class_id = int(box.cls)
                class_name = result.names[class_id]
                score = float(box.conf)
                bbox = box.xyxy[0].tolist()
                detections.append({
                    "bbox": bbox,
                    "score": score,
                    "class_id": class_id,
                    "class_name": class_name,
                })

                
        self.detections = detections
