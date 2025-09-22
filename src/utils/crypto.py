import json
import os
from cryptography.fernet import Fernet

KEY_FILE = "rpi/secret.key"

# -------- Key Handling --------
def generate_key():
    """Generate a key if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    return load_key()

def load_key() -> bytes:
    """Load the key from disk."""
    with open(KEY_FILE, "rb") as f:
        return f.read()

# -------- Encryption --------
def encrypt_json(data: dict, base_filename: str):
    """
    Encrypt a Python dict as JSON and save to <base_filename>.enc.
    If the encrypted file exists, it is replaced.
    """
    key = generate_key()
    cipher = Fernet(key)

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(base_filename), exist_ok=True)

    # Convert dict to JSON bytes
    json_bytes = json.dumps(data).encode("utf-8")

    # Encrypt and save
    encrypted = cipher.encrypt(json_bytes)
    enc_path = f"{base_filename}"
    with open(enc_path, "wb") as f:
        f.write(encrypted)

    print(f"Encrypted JSON saved to {enc_path}")
    return enc_path

# -------- Decryption --------
def decrypt_json(enc_path: str) -> dict:
    """
    Decrypt the encrypted file and return a Python dict.
    """
    key = load_key()
    cipher = Fernet(key)

    with open(enc_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_bytes = cipher.decrypt(encrypted_data)
    return json.loads(decrypted_bytes.decode("utf-8"))

# -------- Example Usage --------
if __name__ == "__main__":
    # Your JSON content
    sample_data = {
        "name": "Alice",
        "age": 30,
        "roles": ["admin", "developer"]
    }

    # Encrypt (will create or overwrite mydata.enc)
    enc_file = encrypt_json(sample_data, "data/mydata.enc.iwl")

    # Decrypt back to Python dict
    result = decrypt_json(enc_file)
    print("Decrypted content:", result)
