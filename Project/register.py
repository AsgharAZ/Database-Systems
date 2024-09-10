import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

class RegisterApp(QtWidgets.QMainWindow):
    def _init_(self):
        super(RegisterApp, self)._init_()
        uic.loadUi('register.ui', self)  # Load your UI file here

        # Access the widgets
        self.name_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.email_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.password_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.confirm_password_line_edit = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.privacy_policy_checkbox = self.findChild(QtWidgets.QCheckBox, 'checkBox')
        self.register_button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        # Connect the register button click to a function
        self.pushButton_2.clicked.connect(self.register_user)

    def register_user(self):
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_4.text()
        confirm_password = self.lineEdit_5.text()
        privacy_accepted = self.checkBox.isChecked()

        # Validate the input fields
        if not name or not email or not password or not confirm_password:
            QMessageBox.warning(self, 'Input Error', 'All fields must be filled in.')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Password Error', 'Passwords do not match.')
            return

        if not privacy_accepted:
            QMessageBox.warning(self, 'Privacy Policy', 'You must accept the privacy policy.')
            return

        # Simulate successful registration
        QMessageBox.information(self, 'Success', f'Registration successful for {name}!')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()