import cv2
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Detection:
    cap = cv2.VideoCapture(0)
    hand_cascade = cv2.CascadeClassifier('hand.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in hands:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('Hand Detection', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

class VideoThread(QThread):
    image_data = pyqtSignal(QImage)

    def __init__(self, video_source=0, parent=None):
        super().__init__(parent)
        self.video_source = video_source

    def run(self):
        cap = cv2.VideoCapture(self.video_source)
        while True:
            ret, frame = cap.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.image_data.emit(qt_image)

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Video Player')
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        self.video_thread = VideoThread()
        self.video_thread.image_data.connect(self.set_image)
        self.video_thread.start()

    def set_image(self, image):
        self.image_label.setPixmap(QPixmap.fromImage(image))

if __name__ == '__main__':
    app = QApplication([])
    player = VideoPlayer()
    player.show()
    app.exec()




# cap = cv2.VideoCapture(0)
# hand_cascade = cv2.CascadeClassifier('hand.xml')
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in hands:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
#     cv2.imshow('Hand Detection', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
