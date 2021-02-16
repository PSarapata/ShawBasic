types_of_people = 10
x = f"Istnieje {types_of_people} rodzajów ludzi."

binary = "binarny"
do_not = "nie_znają"
# 1
y = f"Ci, którzy znają {binary} i ci, którzy go {do_not}."

print(x)
print(y)

# 2
print(f"Powiedziałem: {x}")
# 3
print(f"Powiedziałem również: '{y}'")

hilarious = False
joke_evaluation = "Czyż to nie jest przezabawny dowcip?! {}"

print(joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = 'łańcucha znaków z prawą stroną.'

# 4
print(w + e)

# @3. Fajne pytanie, bo sprawdza czy czytelnik odróżnia typy danych. Tak, są 4, pozostałe to int i boolean.
# @4. Konkatenacja stringów
# Extra: najłatwiej zepsuć kod zmieniając zmienną e na inny typ, np. int - nie można dodać stringa do inta, wyrzuci to TypeError