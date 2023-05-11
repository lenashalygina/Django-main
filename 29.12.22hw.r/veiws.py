from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from django.shortcuts import render
from django.http import JsonResponse
import requests
import sys


def fetch_jsonplaceholder_data(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)


class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Todo App')
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel()
        self.label.setText('Fetching data...')
        self.label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.fetch_data()

    def fetch_data(self):
        try:
            url = 'http://localhost:8000/fetch-data/'
            response = requests.get(url)
            data = response.json()
            self.label.setText(f'Fetched {len(data)} records from JSONPlaceholder API.')
        except Exception as e:
            self.label.setText(f'Error fetching data: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

