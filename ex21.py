def add(a, b):
    print(f"DODAWANIE {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"ODEJMOWANIE {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MNOŻENIE {a} * {b}")
    return a * b

def divide(a, b):
    print("DZIELENIE {a} / {b}")
    return a / b

print("Let's do some calculus just using functions.")

age = add(20, 8)
height = subtract(200, 18)
weight = multiply(35, 2)
iq = divide(9001, 1)

print(f"Wiek: {age}, wzrost: {height}, waga: {weight}, iq: {iq}")

if iq > 9000:
    print("It's over 9000!")

print("This is a task.")
what = add(age, subtract(height, multiply(weight, divide(iq, 9001))))

print(f"That is... {what}")
