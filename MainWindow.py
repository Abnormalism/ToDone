import requests
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea
from PySide6.QtCore import Qt

# Widgets
from Widgets.TodoWidget import TodoWidget
from Widgets.TodoAdd import TodoAdd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.todos = []

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(0, 0, 0, 0)

        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        central_layout.addWidget(scroll_area)

        # Create content widget
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setContentsMargins(10, 10, 10, 10)
        self.content_layout.setSpacing(10)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        content_widget.setAttribute(Qt.WA_StyledBackground, True)
        content_widget.setStyleSheet('background-color: skyblue;')

        # Add TodoAdd widget
        self.todo_add = TodoAdd()
        self.todo_add.todo_add.connect(self.refresh_todos)
        central_layout.addWidget(self.todo_add)

        # Attributes
        self.setFixedSize(400, 400)
        self.setWindowTitle('ToDone')
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.get_todo()
        self.display_todo()

    def display_todo(self):
        for todo in self.todos:
            todo_widget = TodoWidget(todo)
            todo_widget.todo_deleted.connect(self.refresh_todos)
            self.content_layout.addWidget(todo_widget)

    def get_todo(self):
        api = requests.get('http://127.0.0.1:8000/todos')

        if api.status_code == 200:
            self.todos = api.json()

    def refresh_todos(self):
        # Clear existing todos
        while self.content_layout.count() > 0:
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.get_todo()
        self.display_todo()