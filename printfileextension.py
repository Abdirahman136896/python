#Python program to accept a filename from the user and print the extension of that
filename = input("Enter the filename: ")
pos = filename.find(".")
print(filename[pos:])