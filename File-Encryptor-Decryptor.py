import os
import base64

def xor_encrypt_decrypt(data: bytes, key: str) -> bytes:
    """Encrypt or decrypt bytes using XOR."""
    key_bytes = key.encode()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

def encrypt_file(file_path: str, key: str):
    """Encrypt a file using XOR and save as .enc."""
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()

        encrypted_data = xor_encrypt_decrypt(file_data, key)
        encoded_data = base64.b64encode(encrypted_data)

        new_path = file_path + ".enc"
        with open(new_path, "wb") as f:
            f.write(encoded_data)

        print(f"File encrypted successfully: {new_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(file_path: str, key: str):
    """Decrypt a .enc file using XOR."""
    try:
        with open(file_path, "rb") as f:
            encoded_data = f.read()

        encrypted_data = base64.b64decode(encoded_data)
        decrypted_data = xor_encrypt_decrypt(encrypted_data, key)

        new_path = file_path.replace(".enc", "_decrypted")
        with open(new_path, "wb") as f:
            f.write(decrypted_data)

        print(f"File decrypted successfully: {new_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error decrypting file: {e}")

def main():
    while True:
        print("\n--- File Encryption/Decryption Tool ---")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            file_path = input("Enter file path to encrypt: ").strip()
            key = input("Enter encryption key: ").strip()
            if not key:
                print("Error: Key cannot be empty.")
                continue
            encrypt_file(file_path, key)

        elif choice == "2":
            file_path = input("Enter file path to decrypt (.enc file): ").strip()
            key = input("Enter decryption key: ").strip()
            if not key:
                print("Error: Key cannot be empty.")
                continue
            decrypt_file(file_path, key)

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
