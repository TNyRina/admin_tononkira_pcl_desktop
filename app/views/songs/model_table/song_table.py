from PySide6.QtCore import QAbstractTableModel, Qt

class SongTableModel(QAbstractTableModel):

    def __init__(self, songs=None):
        super().__init__()
        self.songs = songs or []

        self.COLUMNS = [
        ('TITRE', 'title'),
        ('DATE DE SORTIE', 'release'),
        ('AUTEUR', 'author'),
        ('COMPOSITEUR', 'composer'),
        ('DESCRIPTION', 'description')
    ]

    def setData(self, songs):
        self.songd = songs or []

    def rowCount(self, parent = None):
        return len(self.songs)
    
    def columnCount(self, /, parent = None):
        return len(self.COLUMNS)
    
    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return None
        
        song = self.songs[index.row()]
        column_attr = self.COLUMNS[index.column()][1]

        if role == Qt.DisplayRole:
            return getattr(song, column_attr)

        if role == Qt.UserRole:
            return song
    
    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.COLUMNS[section][0]
        
