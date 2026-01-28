from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit

class BoxVerses(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()


        """
        Load UI
        =============================
        """
        
        self.ui = parent.get_ui().findChild(QWidget, 'content_verses')




        """
        Buttons add/remove
        =============================
        """
        #Buttton do add verse
        self.btn_push_verse = parent.get_ui().findChild(QPushButton, 'btn_push_verse')
        self.btn_push_verse.clicked.connect(lambda: self._push_verse())

        #Button to delete verse
        self.btn_pop_verse = parent.get_ui().findChild(QPushButton, 'btn_pop_verse')
        self.btn_pop_verse.clicked.connect(lambda: self._pop_verse())



    def _push_verse(self, value: str = None) -> None:
        layout_content = self.ui.layout()

        if layout_content is None:
            layout_content = QVBoxLayout(self.ui)

        index = layout_content.count() + 1

        verse_widget = QWidget()
        verse_layout = QVBoxLayout(verse_widget)

        label = QLabel(f"Verse {index}")
        text = QTextEdit()
        text.setObjectName(f"text_verse_{index}")

        if value :
            text.setPlainText(value)

        verse_layout.addWidget(label)
        verse_layout.addWidget(text)

        layout_content.addWidget(verse_widget)

    def _pop_verse(self) -> None:
        layout = self.ui.layout()

        if layout is None or layout.count() < 1:
            return 

        item = layout.takeAt(layout.count() - 1)
        if item.widget():
            item.widget().deleteLater()

    

    def fill(self, verses: str):
        for verse in verses.split(':') :
            self._push_verse(verse)


    def get_verses(self) -> list[str]:
        layout_verses = self.ui.layout()
        verses = []

        if not layout_verses:
            return verses

        for i in range(layout_verses.count()):
            item = layout_verses.itemAt(i)
            verse_widget = item.widget().layout()
            if verse_widget:
                text_edit = verse_widget.itemAt(1).widget()
                verses.append(text_edit.toPlainText())


        return verses