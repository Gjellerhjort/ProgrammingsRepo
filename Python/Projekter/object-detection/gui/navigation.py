from PyQt6.QtCore import QObject, pyqtSignal

class NavigationController(QObject):
    frame_changed = pyqtSignal(int)

    def __init__(self, num_frames):
        super().__init__()
        self.num_frames = num_frames
        self.current_frame = 0

    def next_frame(self):
        if self.current_frame < self.num_frames - 1:
            self.current_frame += 1
            self.frame_changed.emit(self.current_frame)

    def prev_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.frame_changed.emit(self.current_frame)

    def set_frame(self, idx):
        if 0 <= idx < self.num_frames:
            self.current_frame = idx
            self.frame_changed.emit(self.current_frame)
