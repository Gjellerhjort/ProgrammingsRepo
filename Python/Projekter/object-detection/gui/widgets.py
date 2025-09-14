import cv2
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

class ComparisonWidget(QWidget):
    def __init__(self, parent, detectors, video_path):
        super().__init__(parent)
        self.detectors = detectors
        self.video_path = video_path

        # For each model, show its name above its image
        self.model_layouts = []
        self.model_labels = []
        self.image_labels = []

        self.images_area = QHBoxLayout()

        for i, detector in enumerate(self.detectors):
            vbox = QVBoxLayout()
            model_label = QLabel(detector.__class__.__name__, self)
            model_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_label = QLabel(self)
            image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.model_labels.append(model_label)
            self.image_labels.append(image_label)
            vbox.addWidget(model_label)
            vbox.addWidget(image_label)
            self.model_layouts.append(vbox)
            self.images_area.addLayout(vbox)

        # Navigation buttons
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.prev_button.clicked.connect(self.prev_frame)
        self.next_button.clicked.connect(self.next_frame)

        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.button_layout.addStretch()

        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addLayout(self.images_area)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        # Load frames
        self.frames = self.load_frames(video_path)
        self.frame_idx = 0
        self.update_images()

    def load_frames(self, video_path, max_frames=300):
        cap = cv2.VideoCapture(video_path)
        frames = []
        count = 0
        while True:
            ret, frame = cap.read()
            if not ret or count >= max_frames:
                break
            frames.append(frame)
            count += 1
        cap.release()
        return frames

    def update_images(self):
        if not self.frames:
            for lbl in self.image_labels:
                lbl.setText("No frames")
            return
        frame = self.frames[self.frame_idx]
        image_list = []
        for detector in self.detectors:
            detector.detect(frame)
            annotated = detector.annotate_frame(frame.copy())
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            image_list.append(annotated_rgb)
        self.set_images(image_list)

    def set_images(self, image_list):
        # scale images to label size
        for lbl, img in zip(self.image_labels, image_list):
            if img is not None:
                h, w, ch = img.shape
                bytes_per_line = ch * w
                qimg = QImage(img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                # Use current label size for scaling
                size = lbl.size()
                pixmap = QPixmap.fromImage(qimg)
                lbl.setPixmap(pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            else:
                lbl.setText("No image")

    def resizeEvent(self, event):
        # Rescale images when window is resized
        self.update_images()

    def next_frame(self):
        if self.frame_idx < len(self.frames) - 1:
            self.frame_idx += 1
            self.update_images()

    def prev_frame(self):
        if self.frame_idx > 0:
            self.frame_idx -= 1
            self.update_images()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Right:
            self.next_frame()
        elif event.key() == Qt.Key.Key_Left:
            self.prev_frame()
