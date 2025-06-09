from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Load server's public key
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Get server's public parameters
    parameters = server_public_key.parameters()

    # Generate client's key pair
    private_key, public_key = generate_client_key_pair(parameters)

    # Derive shared secret using client's private key and server's public key
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # Print the shared secret in hexadecimal form
    print("Shared secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
