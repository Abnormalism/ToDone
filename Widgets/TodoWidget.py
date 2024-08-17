import requests
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, Signal

#Widgets
from .Label import Label
from .ActionLayout import ActionLayout

class TodoWidget(QWidget):
    todo_deleted = Signal(int)

    def __init__(self, todos):
        super().__init__()

        #attributes
        self.setObjectName('TodoWidget')
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(60)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        #API

        #Widgets
        label = Label(todos)
        self.h_layout.addWidget(label)

        action_layout = ActionLayout(todos['id'])
        action_layout.todo_deleted.connect(self.on_todo_deleted)
        self.h_layout.addWidget(action_layout, alignment=Qt.AlignmentFlag.AlignRight)

        #Styles
        self.setStyleSheet(
            """
                #TodoWidget {
                    background-color: white;
                    border-radius: 5px;
                }
            """
        )

    def on_todo_deleted(self, todo_id):
        self.todo_deleted.emit(todo_id)