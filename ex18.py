# Just an example of argument unpacking
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg):
    print(f"argument: {arg}")

def print_none():
    print("I take no arguments...")

print_two("Zed", "Shaw")
print_two_again("Pawel", "Sarapata")
print_one("First!")
print_none()
