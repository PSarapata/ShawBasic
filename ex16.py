# Operacje na plikach
# close - zamyka plik (save)
# read - czyta zawartość, wynik można przypisać do zmiennej
# readline - czyta jedną linijkę pliku
# truncate - opróżnia plik
# write('whatever') - zapisuje 'cokolwiek' do pliku
# seek(0) - przesuwa lokalizację odczytu/zapisu na początek pliku.


from sys import argv


script, filename = argv

print(f"We'll wipe {filename}...")
print("If you don't want to, press CTRL + C (^C).")
print("If you want to continue, press ENTER.")

input("?")

print("Opening file...")
target = open(filename, 'w')

# print("Deleting file contents... Bye!") - unnecessary, already done from the get-go whilst opened in 'write' mode
# target.truncate()

print("Now I will ask you to type 3 lines of text:")

line1 = input("first line: ")
line2 = input("second line: ")
line3 = input("third line: ")

print("Imma save it inside my file...")

target.write(line1, '\n')
target.write(line2, '\n')
target.write(line3, '\n')

print("Aaaaand close the file.")
target.close()
