import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow  # Chỉnh đúng tên class trong file ui/rsa.py
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Sửa thành đúng class UI
        self.ui.setupUi(self)

        # Kết nối nút bấm với hàm API
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.show_message("Info", data["message"])
            else:
                self.show_message("Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        plaintext = self.ui.txt_plaintext.toPlainText()  # QTextEdit
        payload = {
            "message": plaintext,
            "key_type": "public"
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setPlainText(data["encrypted_message"])  # QTextEdit
                self.show_message("Info", "Encrypted Successfully")
            else:
                self.show_message("Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        ciphertext = self.ui.txt_ciphertext.toPlainText()  # QTextEdit
        payload = {
            "ciphertext": ciphertext,
            "key_type": "private"
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setPlainText(data["decrypted_message"])  # QTextEdit
                self.show_message("Info", "Decrypted Successfully")
            else:
                self.show_message("Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        message = self.ui.txt_info.toPlainText()  # QTextEdit
        payload = {
            "message": message
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data["signature"])  # QTextEdit
                self.show_message("Info", "Signed Successfully")
            else:
                self.show_message("Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        message = self.ui.txt_info.toPlainText()  # QTextEdit
        signature = self.ui.txt_sign.toPlainText()  # QTextEdit
        payload = {
            "message": message,
            "signature": signature
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    self.show_message("Info", "Verified Successfully")
                else:
                    self.show_message("Info", "Verification Failed")
            else:
                self.show_message("Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"Error: {e}")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
