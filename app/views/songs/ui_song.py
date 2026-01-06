from PySide6.QtWidgets import QPushButton, QWidget
from app.views.songs.ui_form_add import FormAddSongUI
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/songs/song.ui"

class SongUI(QWidget):
    def __init__(self):
        self.ui = load_ui(UI_PATH)

        self.form_add_ui = FormAddSongUI()

        self.btn_to_add_form = self.ui.findChild(QPushButton, "btn_to_add_form")
        self.btn_to_category = self.ui.findChild(QPushButton, "btn_to_category")

    def get_ui(self):
        return self.ui