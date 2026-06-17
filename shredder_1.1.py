#version 1.2
#delete files securely and leave minimal traces of the file including file name which may give out some info like date created 

import os
from cryptography.fernet import Fernet

#encrypt + delete with different keys for each file
def shred(f_path):
    key = Fernet.generate_key()
    try:
        with open(f_path, "rb") as file:
            data = file.read()

        contents = Fernet(key).encrypt(data)

        with open(f_path, "wb") as file:
            file.write(contents)

        new = Fernet(key).encrypt(f_path.encode())
        os.rename(f_path, new)
        os.remove(new)
        print(f"DELETED : {f_path}")


    except Exception as e:
        print(f"Error: {e}")

    finally:
        key = None
        

def main():
    f_path = input ("Path:- ")
    if os.path.isdir(f_path):
        for i in os.listdir(f_path):
            shred(os.path.join(f_path,i))
        os.rmdir(f_path)
        print("DONE\n")
    
    else:
        shred(f_path)
        print("DONE\n")

if __name__ == "__main__":
    main()
