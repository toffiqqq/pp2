import os 

#1
def filesAndDirs(path):
    all = os.listdir(path)
    dirs = [i for i in all if os.path.isdir(os.path.join(path, i))]
    files = [i for i in all if os.path.isfile(os.path.join(path, i))]
    print(f"All directories in {path}: {dirs}")
    print(f"Only files in {path}: {files}")
    
path = input("Enter a path: ")
filesAndDirs(path)

#2
def access(path):
    if os.path.exists(path):
        print(f"Yes, path {path} exists")
    else:
        print(f"No,path {path} doesnt exists")

    if os.access(path, os.W_OK):
        print(f"The path {path} are writable")
    else:
        print(f"No,path {path} are not writable")

    if os.access(path, os.X_OK):
        print(f"The path {path} are excecutable")
    else:
        print(f"No,path {path} are not executable")
    
path = input("Enter a path: ")
access(path)

#3
def test_path(path):
    if os.path.exists(path):
        print(f"Yes, path {path} exists, filname: {os.path.basename}, dirname: {os.path.dirname}")
    else:
        print(f"No,path {path} doesnt exists")

path = input("Enter a path: ")
test_path(path)

#4
with open("file.txt", "r") as f:
    lines = f.readline()
    print(len(lines))
    
#5
list = ['ab', 'bc', 'cd', 'de']
with open('file.txt', 'w') as file:
    for item in list:
        file.write(item + '\n')

#6
import string
def creatFiles():
    for letter in string.ascii_uppercase:
        with open(letter + ".txt","w") as g:
            g.write(letter)
creatFiles()

#7
with open("firstFile.txt",'r') as first, open('secondFile.txt','w') as second:
    for line in first:
        second.write(line)

#8
def remove_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File is removed succesfully")
        else:
            print("This file is not accesible")
    else:
        print(f"No, path {path} doesnt exists")
path = input("Enter your path name: ")
remove_file(path)