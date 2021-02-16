from os import O_TRUNC
from sys import argv

script, filename = argv

txt = open(filename)

print(f"This is your file: {filename}.")
print(txt.read())

print("Repeat filename please: ")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()
