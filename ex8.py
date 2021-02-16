formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("jeden", "dwa", "trzy", "cztery"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Wlazł kotek",
    "na płotek i mruga.",
    "Ładna to piosenka,",
    "nie długa."
))