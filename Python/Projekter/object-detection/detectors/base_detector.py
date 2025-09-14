import numpy as np
import cv2
from typing import List, Dict, Any
from abc import ABC, abstractmethod

class BaseDetector(ABC):
    """
    Abstract base class for person detectors.
    All detectors should inherit from this class and implement the detect method.
    """

    def __init__(self, model_path: str = None, device: str = "gpu", conf_threshold: float = 0.3):
        self.model_path = model_path
        self.device = device
        self.conf_threshold = conf_threshold
        self.model = None
        self.detections = []

    @abstractmethod
    def load_model(self):
        """Load the detection model from file/model hub."""
        pass

    @abstractmethod
    def detect(self, image: np.ndarray):
        """
        Perform person detection on an input image.

        Args:
            image (np.ndarray): Input image in BGR or RGB format.

        Returns:
            List[Dict[str, Any]]: List of detections.
                Each detection is a dict with keys:
                - 'bbox': [x1, y1, x2, y2]
                - 'score': float
                - 'class_id': int
                - 'class_name': str
        """
        pass

    def get_detections(self) -> List[Dict[str, Any]]:
        return self.detections

    def annotate_frame(self, image: np.ndarray) -> np.ndarray:
        """Annotate image with bounding boxes and labels."""
        for det in self.detections:
            x1, y1, x2, y2 = map(int, det['bbox'])
            label = f"{det['class_name']} {det['score']:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        return image


