# REVISION

escape_sequences = """
\\ - backslash
\' - single quote
\" - double quote
\a - ASCII BEL sign (dźwięk alertu np. w drukarkach, coś nowego)
\b - ASCII BS (backspace) sign
\f - ASCII FF sign (Form Feed) (znak "wysunięcia strony", coś nowego)
\n - new line symbol
\N(name) - sign with name name from Unicode database... (woot?)
\r - Carriage Return - CR
\t - TAB (horizontal tab)
\uxxxx - sign representing 16bit hexadecimal value
\Uxxxxxxxx - sign representing 32bit hexadecimal value
\v - ASCII VT (vertical tab)
\ooo - sign representing octal value
\xhh - sign representing hex value
"""

print("How old are you?", end=' ') #  Overwriting default new line finish, quite useful

"""
from sys import argv

script, first, second, third = argv
"""
#  Similar to *args unpacking, except that it is done from terminal level. When starting the script we specify additional variables
#  e.g. python script.py first second third, those then get passed to argv as arguments.

"from os.path import exists"  # checks if a file exists
"file.seek(0)"  # sets caret at byte 0 of the target file
