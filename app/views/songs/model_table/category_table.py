from PySide6.QtCore import Qt, QAbstractTableModel

class CategoryTableModel(QAbstractTableModel) :
    def __init__(self, categories=None):
        super().__init__()
        self.categories = categories or []

    def setData(self, categories):
        self.categories = categories or []
    
    def rowCount(self, parent = None):
        return len(self.categories)

    def columnCount(self, parent = None):
        return 1
    
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        category = self.categories[index.row()]

        if role == Qt.DisplayRole:    
            return category.name

        if role == Qt.UserRole:
            return category
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        headers = ["Categorie"]

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return headers[section]
        
    
