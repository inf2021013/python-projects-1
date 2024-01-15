import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QKeySequence

class TextEditor(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a QTextEdit widget and set it as the central widget
        # of the main window
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Create a "save" action
        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_text)

        # Add the action to the File menu
        self.file_menu = self.menuBar().addMenu("File")
        self.file_menu.addAction(save_action)

    def save_text(self):
        text = self.text_edit.toPlainText()
        with open("text.txt", "w") as f:
            f.write(text)

app = QApplication(sys.argv)
editor = TextEditor()
editor.show()
sys.exit(app.exec_())
