# 1. Import các thư viện cần thiết
from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher # Giả định CaesarCipher được định nghĩa trong cipher/caesar.py

# 2. Khởi tạo ứng dụng Flask
app = Flask(__name__)

# 3. Router routes cho trang chủ
@app.route("/")
def home():
    """
    Hiển thị trang chủ của ứng dụng.
    """
    return render_template('index.html')

# 4. Router routes cho caesar cypher
@app.route("/caesar")
def caesar():
    """
    Hiển thị trang giao diện Caesar Cipher.
    """
    return render_template('caesar.html')

# 5. Endpoint API để mã hóa Caesar Cipher
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    """
    Mã hóa văn bản bằng thuật toán Caesar Cipher.
    Chấp nhận yêu cầu POST với form data: 'inputPlainText' và 'inputKeyPlain'.
    Trả về văn bản đã mã hóa cùng với văn bản gốc và khóa.
    """
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher() # Tạo một đối tượng CaesarCipher
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# 6. Endpoint API để giải mã Caesar Cipher
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    """
    Giải mã văn bản bằng thuật toán Caesar Cipher.
    Chấp nhận yêu cầu POST với form data: 'inputCipherText' và 'inputKeyCipher'.
    Trả về văn bản đã giải mã cùng với văn bản đã mã hóa và khóa.
    """
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher() # Tạo một đối tượng CaesarCipher
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# 7. Hàm main để chạy ứng dụng
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)