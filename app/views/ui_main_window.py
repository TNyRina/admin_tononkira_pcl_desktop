from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from app.views.utility.navigation import Navigation
from app.views.ui_sidebar import SidebarUI
from app.views.ui_main_content import MainContentUI

class MainWindow(QMainWindow):
    def __init__(self, title: str, session):
        super().__init__()
        self.setWindowTitle(title)
        self.showMaximized() 
        
        self.sidebar = SidebarUI()
        self.stack = MainContentUI(session)

        Navigation(stack=self.stack, sidebar=self.sidebar).setup()
        
        self._display_setup()

         

    def _display_setup(self) -> None:
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout horizontal
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        layout.addWidget(self.sidebar.get_ui())
        layout.addWidget(self.stack.get_ui())

        layout.setStretch(0, 1)  
        layout.setStretch(1, 4) 
