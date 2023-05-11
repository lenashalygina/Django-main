from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Select a file', self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.show_file_dialog)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(100, 200, 200, 200)

    def show_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select a file', '', 'Text files (*.txt)')

        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setText(file.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 400)
    window.show()
    sys.exit(app.exec())
