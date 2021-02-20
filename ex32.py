# lists and iterating over them...

hairs = ['brązowe', 'blond', 'rude']
eyes = ['brązowe', 'niebieskie', 'zielone']
weights = [1, 2, 3, 4]

the_count = range(6)
fruits = ['jabłka', 'pomarańcze', 'gruszki', 'morele']
change = [1, 'jednogroszówki', 2, 'dwugroszówki', 3, 'pięciogroszówki']

for number in the_count:
    print(f"This is number {number}")

for fruit in fruits:
    print(f"This is {fruit}")

for i in change:
    print(f"I got {i}")

elements = []
print(f"Elements list initialized: {elements}")

for i in range(1,6):
    print(f"Let's add {i} to our list of elements.")
    elements.append(i)

print(f"State of elements list: {elements}")
