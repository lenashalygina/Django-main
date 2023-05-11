from rest_framework import viewsets
from serializers import TodoItemSerializer
from models import TodoItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLineEdit, QPushButton
import requests


class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up UI
        self.setWindowTitle('Todo List')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.todo_list = QListWidget()
        layout.addWidget(self.todo_list)

        self.new_todo_input = QLineEdit()
        layout.addWidget(self.new_todo_input)

        add_todo_button = QPushButton('Add Todo')
        layout.addWidget(add_todo_button)

        delete_todo_button = QPushButton('Delete Todo')
        layout.addWidget(delete_todo_button)

        update_todo_button = QPushButton('Update Todo')
        layout.addWidget(update_todo_button)

        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        add_todo_button.clicked.connect(self.add_todo)
        delete_todo_button.clicked.connect(self.delete_todo)
        update_todo_button.clicked.connect(self.update_todo)

        # Load todo items from backend
        self.load_todo_items()

    def load_todo_items(self):
        response = requests.get('http://localhost:8000/api/todo-items/')
        self.todo_list.clear()
        self.todo_list.addItems([item['title'] for item in response.json()])

    def add_todo(self):
        new_todo_title = self.new_todo_input.text()
        if new_todo_title:
            response = requests.post('http://localhost:8000/api/todo-items/', data={'title': new_todo_title})
            if response.status_code == 201:
                self.load_todo_items()
                self.new_todo_input.clear()

    def delete_todo(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            todo_title = selected_item.text()
            response = requests.delete(f'http://localhost:8000/api/todo-items/{todo_title}/')
            if response.status_code == 204:
                self.load_todo_items()

    def update_todo(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            todo_title = selected_item.text()
            completed = selected_item.checkState() == 2
            data = {'title': todo_title, 'completed': completed}
            response = requests.put(f'http://localhost:8000/api/todo-items/{todo_title}/', json=data)
            if response.status_code == 200:
                self.load_todo_items()


if __name__ == '__main__':
    app = QApplication([])
    window = TodoListApp()
    window.show()
    app.exec()
