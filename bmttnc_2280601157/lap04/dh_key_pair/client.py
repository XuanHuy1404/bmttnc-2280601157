from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Sinh cặp khóa client từ tham số DH
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Tính shared secret từ private key và server public key
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Load server's public key từ file PEM
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy parameters từ server's public key
    parameters = server_public_key.parameters()

    # Sinh cặp khóa client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính shared secret
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret (hex):", shared_secret.hex())

if __name__ == "__main__":
    main()
