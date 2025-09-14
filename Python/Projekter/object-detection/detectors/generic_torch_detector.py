import numpy as np
import torch
import torchvision
from detectors.base_detector import BaseDetector

COCO_CLASSES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag',
    'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

class GenericTorchDetector(BaseDetector):
    def __init__(self, model_class, class_names=None, device='cuda', **model_kwargs):
        super().__init__()
        self.model_class = model_class
        self.model_kwargs = model_kwargs
        self.device = device
        self.class_names = "person"
        self.model = None

    def load_model(self):
        self.model = self.model_class(**self.model_kwargs)
        self.model.eval()
        self.model.to(self.device)

    def detect(self, image: np.ndarray):
        img_tensor = torch.from_numpy(image).permute(2, 0, 1).float() / 255
        img_tensor = img_tensor.unsqueeze(0).to(self.device)
        with torch.no_grad():
            outputs = self.model(img_tensor)[0]

        detections = []
        for bbox, score, label in zip(outputs['boxes'], outputs['scores'], outputs['labels']):
            if score < self.conf_threshold:
                continue
            bbox = bbox.cpu().numpy().tolist()
            class_id = label.item()
            class_name = self.class_names[class_id] if self.class_names and class_id < len(self.class_names) else str(class_id)
            detections.append({
                "bbox": bbox,
                "score": score.item(),
                "class_id": class_id,
                "class_name": class_name,
            })
        self.detections = detections


class FasterRCNNDetector(GenericTorchDetector):
    def __init__(self):
        super().__init__(
            model_class=torchvision.models.detection.fasterrcnn_resnet50_fpn,
            pretrained=True
        )

class SSDDetector(GenericTorchDetector):
    def __init__(self):
        super().__init__(
            model_class=torchvision.models.detection.ssd300_vgg16,
            pretrained=True
        )
