#version 1.1

import os
from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key()

    path = input ("Enter file path: ")

    try:
        with open(path, "rb") as file:
            data = file.read()

        contents = Fernet(key).encrypt(data)

        with open(path, "wb") as file:
            file.write(contents)

        os.remove(path)


    except Exception as e:
        print(f"Error: {e}")

    finally:
        key = None
        print("done")

if __name__ == "__main__":
    main()