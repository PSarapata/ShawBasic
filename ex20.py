from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First we'll print the entire file:\n")

print_all(current_file)

print("Now, let us rewind to the beginning...")

rewind(current_file)

print("Let us print 3 lines:")

for curr_line in range(1,4):
    print_a_line(curr_line, current_file)
current_file.close()
