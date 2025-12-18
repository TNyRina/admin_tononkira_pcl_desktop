from PySide6.QtWidgets import QStackedWidget   
from app.views.songs.ui_song import SongUI
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/content.ui"

class MainContentUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        self.dashboard_ui = load_ui("app/ui/dashboard.ui")
        self.song_ui = SongUI()

        self.addWidget(self.dashboard_ui)
        self.addWidget(self.song_ui.get_ui())

        self.setCurrentWidget(self.dashboard_ui)


    
    def get_ui(self):
        return self