class Navigation:
    def __init__(self, sidebar, content_main):
        self.sidebar = sidebar
        self.content_main = content_main


    def setup(self):
        self._sidebar_navigation_setup()
        self._song_navigation_setup()

    def _sidebar_navigation_setup(self):
        self.sidebar.dashboard_btn.clicked.connect(
            lambda: self.content_main.setCurrentWidget(self.content_main.dashboard_ui)
        )

        self.sidebar.song_btn.clicked.connect(
            lambda: self.content_main.setCurrentWidget(self.content_main.song_ui.get_ui())
        )

    def _song_navigation_setup(self):
        self.content_main.addWidget(self.content_main.song_ui.form_add_ui.get_ui())
        self.content_main.song_ui.add_form_btn.clicked.connect(
            lambda: self.content_main.setCurrentWidget(self.content_main.song_ui.form_add_ui.get_ui())
        )