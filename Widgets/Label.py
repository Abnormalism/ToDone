from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class Label(QLabel):
    def __init__(self, todo):
        super().__init__()

        #Attributes
        self.todo = todo

        # Settings
        self.setText(self.todo['title'])
        self.setObjectName('Label')
        self.setAttribute(Qt.WA_StyledBackground)

        #Styles
        self.setStyleSheet(
            """
                #Label {
                    background-color: white;
                }
            """
        )