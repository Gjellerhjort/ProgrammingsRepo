from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout

def get_layout(layout_type="horizontal", widgets=None):
    if widgets is None:
        widgets = []
    if layout_type == "horizontal":
        layout = QHBoxLayout()
    elif layout_type == "vertical":
        layout = QVBoxLayout()
    elif layout_type == "grid":
        layout = QGridLayout()
        for idx, widget in enumerate(widgets):
            row, col = divmod(idx, 2)
            layout.addWidget(widget, row, col)
        return layout
    else:
        layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    return layout
