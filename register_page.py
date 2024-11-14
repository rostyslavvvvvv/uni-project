from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from login_page import LoginPage


class RegisterPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Store the reference to the MainAuth window
        self.setWindowTitle("Sign up to start listening")
        self.setGeometry(100, 100, 300, 250)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Username input
        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        # Password input
        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Confirm password input
        self.confirm_password_label = QLabel("Confirm Password")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        # Register button
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_user)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password == confirm_password:
            print("Registration successful!")
            # After successful registration, go back to the login page
            self.go_to_login()
        else:
            print("Passwords do not match!")

    def go_to_login(self):
        # Close RegisterPage and show LoginPage
        self.main_window.show()  # Show the MainAuth window again
        self.close()  # Close the RegisterPage window