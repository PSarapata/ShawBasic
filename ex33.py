# While loop: the magic behind looping for as long as the condition is true.

i = 0
numbers = []
end_seq = 6
jump_seq = 3

while i <= end_seq:
    print(f"Previous value of i was: {i}")
    numbers.append(i)
    i += jump_seq
    print(f"Current numbers are: {numbers}")
    print(f"Current value of i is: {i}")

print("\n\n\nThe numbers are...")
for num in numbers:
    print(num, end=' ')


#  Second approach: for and range
numbers = []
for i in range(0, end_seq + 1, jump_seq):
    numbers.append(i)

print("\n\nAnd now the numbers are...")
for num in numbers:
    print(num, end=' ')

print("The same!")
