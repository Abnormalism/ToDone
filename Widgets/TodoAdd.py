import requests
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit
from PySide6.QtCore import Qt, Signal

from .Delete import DeleteBtn

class TodoAdd(QWidget):
    todo_add = Signal(dict)

    def __init__(self):
        super().__init__()

        self.setFixedHeight(50)
        self.setContentsMargins(0, 0, 0, 0)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('background-color: white;')
        self.v_layout = QHBoxLayout()
        self.setLayout(self.v_layout)

        self.line_edit = QLineEdit()
        self.v_layout.addWidget(self.line_edit)

        add_btn = DeleteBtn(text='add', color='green')
        add_btn.pressed.connect(self.create_todo)
        self.v_layout.addWidget(add_btn)

    def create_todo(self):
        text = self.line_edit.text()
        api = requests.post('http://127.0.0.1:8000/todos/create', json={'title': text})
        new_todo = api.json()

        self.line_edit.clear()

        if api.status_code == 200:
            self.todo_add.emit(new_todo)