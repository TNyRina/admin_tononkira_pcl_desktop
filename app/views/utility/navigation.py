from PySide6.QtWidgets import QWidget

class Navigation:
    def __init__(self, stack: QWidget, sidebar:QWidget=None):
        self.sidebar = sidebar
        self.stack = stack


    def goto(self, widget: QWidget) -> None:
        self.stack.setCurrentWidget(widget)

    def setup(self) -> None:
        self.sidebar.dashboard_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.stack.dashboard_ui)
        )

        self.sidebar.song_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.stack.song_ui.get_ui())
        )
        
