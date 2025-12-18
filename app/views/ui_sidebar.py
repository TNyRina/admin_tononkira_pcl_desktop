from PySide6.QtWidgets import QFrame, QPushButton
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/sidebar.ui"

class SidebarUI(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        self.dashboard_btn = self.ui.findChild(QPushButton, "dashboard_btn")
        self.song_btn = self.ui.findChild(QPushButton, "lyric_btn")

    
    def get_ui(self):
        return self.ui