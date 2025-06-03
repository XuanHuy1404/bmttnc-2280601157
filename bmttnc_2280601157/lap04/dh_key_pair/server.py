from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Hàm sinh tham số DH (Diffie-Hellman)
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

# Hàm sinh cặp khóa server từ tham số DH
def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm main
def main():
    # Sinh tham số DH
    parameters = generate_dh_parameters()

    # Sinh cặp khóa server
    private_key, public_key = generate_server_key_pair(parameters)

    # Lưu public key ra file PEM
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Chạy chương trình
if __name__ == "__main__":
    main()
