import os

def pack_file():
    file_name = input("Please enter the name of the EXE file you want to pack: ")
    file_size = int(input("How large would you like to pack this file (in bytes)? "))
    
    with open(file_name, 'wb') as f:
        f.write(b'\0' * file_size)
    
    # Set the file size to the packed size
    os.truncate(file_name, file_size)

pack_file()
