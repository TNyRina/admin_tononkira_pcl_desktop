from PySide6.QtWidgets import QWidget
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/form_add.ui"

class FormAddSongUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui(UI_PATH)

    def get_ui(self):
        return self.ui