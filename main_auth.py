from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
from login_page import LoginPage
from register_page import RegisterPage

class MainAuth(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music App - Login/Register")
        self.setGeometry(100, 100, 300, 150)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.open_login_page)
        layout.addWidget(self.login_button)

        # Register button
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.open_register_page)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def open_login_page(self):
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()  # Close main window

    def open_register_page(self):
        self.register_page = RegisterPage(self)  # Pass self (MainAuth instance) to RegisterPage
        self.register_page.show()
        self.close()  # Close main window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_auth = MainAuth()
    main_auth.show()
    sys.exit(app.exec_())