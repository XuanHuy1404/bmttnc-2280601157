from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher  # Import chuẩn ở đầu file

app = Flask(__name__)

# Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()

# Caesar Encrypt
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    print("Received plain_text:", data['plain_text'])  # In giá trị trước khi gán
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypt_text})


# Caesar Decrypt
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypt_text})

# # Vigenere Encrypt
# @app.route('/api/vigenere/encrypt', methods=['POST'])
# def vigenere_encrypt():
#     data = request.json
#     plain_text = data['plain_text']
#     key = data['key']
#     encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
#     return jsonify({'encrypted_text': encrypted_text})

# # Vigenere Decrypt
# @app.route('/api/vigenere/decrypt', methods=['POST'])
# def vigenere_decrypt():
#     data = request.json
#     cipher_text = data['cipher_text']
#     key = data['key']
#     decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
#     return jsonify({'decrypted_text': decrypted_text})

# Chỉ duy nhất 1 lần run app ở cuối file
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
