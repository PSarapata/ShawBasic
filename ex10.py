# Znaki specjalne i escape sequences

tabby_cat = "\tJestem tabulatorem."
persian_cat = "Jestem podziałem \n linii."
backslash_cat = "Escape sequences dla \\ backslasha \\ to dwa backslashe."

fat_cat = """
Zrobię listę:
\t* Jedzenie dla kotka
\t* Rybki
\t* Kocimiętka\n\t* Trawa
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

formatter = "{} {} {} {}"
print(formatter.format((fat_cat), '\n', '\t*ListElement\n', '\x42'))

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
