from PySide6.QtWidgets import QPushButton, QWidget
from app.views.songs.ui_form_add import FormAddSongUI
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/songs/song.ui"

class SongUI(QWidget):
    def __init__(self):
        self.ui = load_ui(UI_PATH)

        self.form_add_ui = FormAddSongUI()

        self.add_form_btn = self.ui.findChild(QPushButton, "add_form_btn")

    def get_ui(self):
        return self.ui