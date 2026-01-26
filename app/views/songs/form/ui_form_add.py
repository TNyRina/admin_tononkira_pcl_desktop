from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit,QLineEdit, QMessageBox
from app.controllers.song_controller import SongController
from app.views.songs.form.box_categories import BoxCategories
from app.views.songs.form.box_verses import BoxVerses
from app.views.user_dialog.dialog_error import ErrorDialog
from app.views.utility.utils import load_ui

UI_PATH = "app/ui/songs/form_add.ui"

class FormAddSongUI(QWidget):
    def __init__(self, session, stack: QWidget, parent: QWidget):
        super().__init__()

        """
        Data controller
        ============================
        """
        self.controller = SongController(session)
        


        """
        Load widget
        ================================
        """
        
        self.stack = stack
        self.ui = load_ui(UI_PATH)
        self.stack.addWidget(self.ui)

        self.parent = parent


        """
        Form
        ===========================================
        """
    

        #Inputs
        self.input_title = self.ui.findChild(QLineEdit, 'input_title')
        self.input_author = self.ui.findChild(QLineEdit, 'input_author')
        self.input_composer = self.ui.findChild(QLineEdit, 'input_composer')
        self.input_description = self.ui.findChild(QTextEdit, 'text_description')
        self.input_refrain = self.ui.findChild(QTextEdit, 'text_refrain')

        #Verses management
        self.verses = BoxVerses(parent=self)

        #Categories options
        self.categories = BoxCategories(session=session, parent=self)
        
        #Button to save song
        self.btn_save = self.ui.findChild(QPushButton, 'btn_save')
        self.btn_save.clicked.connect(lambda: self.save_song())



    def get_ui(self) -> QWidget:
        return self.ui
    


    def save_song(self):
        title = self.input_title.text()
        author = self.input_author.text()
        composer = self.input_composer.text()
        description = self.input_description.toPlainText()
        refrain = self.input_refrain.toPlainText()
        verses = self.verses.get_verses()
        selected_categories = self.categories.get_selected_boxes()

        try:
            self.controller.add_song(
                title=title,
                release="",
                author=author,
                composer=composer,
                description=description,
                refrain=refrain,
                verse=verses,
                categories=selected_categories
            )
            QMessageBox.information(
                    self,
                    "Succès",
                    f"Lyric '{title}' a été ajoutée avec succès."
                )
            
            self.parent.nagivate.goto(self.parent.get_ui())
            self.parent.table.reset()
        except Exception as e:
            error_dialog = ErrorDialog(self, type='warning', exception=e)
            error_dialog.show()


   
