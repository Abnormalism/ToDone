from functools import partial

import requests
from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCore import Qt, Signal

#Widgets
from .Delete import DeleteBtn

class ActionLayout(QWidget):
    todo_deleted = Signal(int)  # Add this line

    def __init__(self, todo_id):
        super().__init__()

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.setContentsMargins(0, 0, 0, 0)

        #Attributes
        self.setObjectName('ActionLayout')
        self.setAttribute(Qt.WA_StyledBackground, True)

        #Widgets
        delete_btn = DeleteBtn('del', 'red')
        delete_btn.clicked.connect(partial(self.delete_todo, todo_id))
        v_layout.addWidget(delete_btn)

        #Styles
        self.setStyleSheet("""
            #ActionLayout {
                background-color: white;
            }
        """)

    def delete_todo(self, todo_id):
        api = requests.delete(f'http://127.0.0.1:8000/todos/delete?id={todo_id}')

        if api.status_code == 200:
            print('deleted')
            self.todo_deleted.emit(todo_id)  # Add this line

