from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class DeleteBtn(QPushButton):
    def __init__(self, text, color):
        super().__init__()

        #Attributes
        self.btn_text = text
        self.btn_color = color

        # Settings
        self.setObjectName('BtnSettings')
        self.setText(self.btn_text)
        self.setFixedWidth(40)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Styles
        self.setStyleSheet(
            f"""
                  #BtnSettings {{
                      background-color: {self.btn_color};
                  }}
                  """
        )