#version 2.0

import os
import hashlib
from cryptography.fernet import Fernet

#folders
def shred_dir(current_path, dir):
    old = os.path.join(current_path, dir)
    new = os.path.join(current_path, hashlib.sha3_512(dir.encode()).hexdigest())
    os.rename(old, new)
    os.rmdir(new)
    print(f"DELETED : {old}")


#encrypt and delete files
def shred(f_path):
    key = Fernet.generate_key()
    try:
        with open(f_path, "rb") as file:
            data = file.read()

        contents = Fernet(key).encrypt(data)

        with open(f_path, "wb") as file:
            file.write(contents)

        #reaname and delete file
        new = hashlib.sha3_512(f_path.encode()).hexdigest()
        os.rename(f_path, new)
        os.remove(new)
        print(f"DELETED : {f_path}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        key = None

#main function
def main():
    f_path = input("Path:- ")
    #checkif path is correct/exists
    try:
        if os.path.exists(f_path):#true
            #dir
            if os.path.isdir(f_path):
                for current_path, folders, files in os.walk(f_path, topdown=False):
                    #access files and encrypt
                    for file in files:
                        shred(os.path.join(current_path,file))
                        print(f"DELETED : {file}")

                    # encrypt folder name
                    for dir in folders:
                        shred_dir(current_path, dir)

                #delete parent
                split_path = f_path.split("/",-1)
                dir = split_path[-1]
                split_path.pop(-1)
                joint = "/".join(split_path)
                shred_dir(current_path=joint, dir=dir)

            # file
            else:
                shred(f_path)
            
            print("DONE\n")
        #false
        else:
            print(f"ERROR: path not found: '{f_path}'")

    except Exeption as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()

