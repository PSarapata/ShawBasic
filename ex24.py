print("More practice.")
print('Let us use escape sequences \\ that insert:')
print('\n new lines and \t tabs')

poem = """
\t This beautiful world
with its' strict logics
cannot see the \n love calling
nor the passion for the feeling
and it needs explanation,
\n\t\tyet there is none.
"""

print('-------------------')
print(poem)
print('-------------------')


five = 10 - 2 + 3 -6
print(f"This should equal {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("Let us start with the initial value: {}".format(start_point))
print(f"It shall give us {int(beans)} beans, {int(jars)} jars and {int(crates)} crates.")


# THIS IS PURE GOLD!!! HOW TO unpack and use the results of the function
start_point = start_point / 10
formula = secret_formula(start_point)
print("This shall give us {} beans, {} jars and {} crates".format(*formula))
