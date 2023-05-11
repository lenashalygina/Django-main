import asyncio
import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Асинхронная загрузка изображений")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 5)
        layout.addWidget(self.progress_bar)

        self.image_labels = []
        for i in range(5):
            label = QLabel()
            layout.addWidget(label)
            self.image_labels.append(label)

        asyncio.ensure_future(self.load_images())

    async def load_images(self):
        urls = [
            "https://picsum.photos/200/300",
            "https://picsum.photos/250/350",
            "https://picsum.photos/300/400",
            "https://picsum.photos/350/450",
            "https://picsum.photos/400/500",
        ]

        tasks = []
        for i, url in enumerate(urls):
            task = asyncio.create_task(self.load_image(url, i))
            tasks.append(task)

        await asyncio.gather(*tasks)

    async def load_image(self, url, index):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                image_bytes = await resp.read()

        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)

        self.image_labels[index].setPixmap(pixmap)

        self.progress_bar.setValue(index + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    asyncio.get_event_loop().run_until_complete(asyncio.gather(window.load_images()))
    sys.exit(app.exec())

