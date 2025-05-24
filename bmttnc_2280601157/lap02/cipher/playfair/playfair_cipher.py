class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Chia thành cặp, thêm 'X' nếu cần
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = ''
            if i + 1 < len(plain_text):
                b = plain_text[i + 1]
            else:
                b = 'X'

            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text

    def clean_decrypted_text(self, decrypted_text):
        banro = ""

        i = 0
        while i < len(decrypted_text) - 2:
            if decrypted_text[i + 1] == 'X' and decrypted_text[i] == decrypted_text[i + 2]:
                banro += decrypted_text[i]
                i += 2
            else:
                banro += decrypted_text[i] + decrypted_text[i + 1]
                i += 2

        # Xử lý 2 ký tự cuối
        if len(decrypted_text) % 2 == 0:
            if decrypted_text[-1] != 'X':
                banro += decrypted_text[-2] + decrypted_text[-1]
            else:
                banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-1]

        return banro
