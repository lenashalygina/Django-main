import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desktop App")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout()
        container.setLayout(layout)

        label = QLabel("Заголовок приложения")
        layout.addWidget(label)

        nav_label = QLabel("Навигация:")
        layout.addWidget(nav_label)

        nav_links = ["Главная", "О нас", "Контакты"]
        for link in nav_links:
            nav_link_label = QLabel(f"<a href='#'>{link}</a>")
            nav_link_label.setOpenExternalLinks(True)
            layout.addWidget(nav_link_label)

        section1_label = QLabel("Секция 1")
        section1_content = QLabel("Содержимое секции 1...")
        layout.addWidget(section1_label)
        layout.addWidget(section1_content)

        section2_label = QLabel("Секция 2")
        section2_content = QLabel("Содержимое секции 2...")
        layout.addWidget(section2_label)
        layout.addWidget(section2_content)

        footer_label = QLabel("Все права защищены &copy; 2023")
        layout.addWidget(footer_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
