from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Gestion Choral")
window.resize(800, 600)
window.show()

app.exec()
