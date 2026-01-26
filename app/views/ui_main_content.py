from PySide6.QtWidgets import QStackedWidget, QWidget   
from app.views.songs.ui_song import SongUI
from app.views.utility.utils import load_ui


UI_PATH = "app/ui/content.ui"

class MainContentUI(QStackedWidget):
    def __init__(self, session):
        super().__init__()
        self.ui = load_ui(UI_PATH)

        """
        Pages setup 
        ====================================================
        """
        
        #dashboard page
        self.dashboard_ui = load_ui("app/ui/dashboard.ui")
        self.addWidget(self.dashboard_ui)

        #song page
        self.song_ui = SongUI(session=session, stack=self)

        #default page
        self.setCurrentWidget(self.dashboard_ui)
        


    
    def get_ui(self) -> QWidget:
        return self