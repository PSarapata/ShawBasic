from sys import argv
script, user_name = argv
prompt = '>>> '

print(f"Hello {user_name}, I am a script called {script}.")
print("I wish to ask you a few questions.")
print(f"Do you like Python, {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What computer have you got?")
computer = input(prompt)

print(f"""
Ok, I asked you whether you like Python, your answer was: {likes}.
You live in {lives}. I'm not sure where that is.
And you've got {computer}. Cool.
""")
