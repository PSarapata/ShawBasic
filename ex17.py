from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")

in_file = open(from_file)
in_data = in_file.read()

print(f"Input file has {len(in_data)} bytes.")

print(f"Does the output file exist? {exists(to_file)}")
input("Press RETURN to continue or CTRL + C to abort.")

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright then, done.")

out_file.close()
in_file.close()
