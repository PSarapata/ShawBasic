ten_things = 'Apples Oranges Crows Phone Light Sugar'

print("Wait a minute, that ain't 10 things! Let's fix this.")

stuff = ten_things.split(' ')

more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Adding: {next_one}")
    stuff.append(next_one)
    print(f"Now there are {len(stuff)} elements in the list.")

print("Now we got it: ", stuff)

print("Let's do some more stuff.")

#  Oranges
print(stuff[1])
# Whatever was last on the list, that should be Corn
print(stuff[-1])
# Take last one out, print it out (Corn)
print(stuff.pop())
# This is 'unpacking' list to a string chain
print(' '.join(stuff))
# Make a string chain from a slice.
print('#'.join(stuff[3:5]))
