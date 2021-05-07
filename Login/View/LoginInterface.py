from PyQt5.QtWidgets import QDialog
from Sicurezza.Login.View.login import Ui_Dialog


class LoginInterface(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.login = Ui_Dialog()
        self.login.setupUi(self)
        self.show()