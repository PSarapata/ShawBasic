people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should be driving cars!")
elif cars < people:
    print("We should not be driving cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("There are too many trucks!")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Okay, let's stay at home.")

# 1. elif to instrukcja warunkowa, która wykona się w przypadku gdy instrukcja if wyrzuciła Fałsz. Interpreter sprawdza warunek,
#    jeśli jest prawdą to wykona kod, jeśli nie - idzie dalej, do else (w else już nie ma warunku, to kod, który wykona się jeśli wszystkie
#    poprzedzające warunki to fałsz). Jeśli wiele elif-ów daje prawdę, wykonany zostanie ten, który wyrzucił prawdę jako pierwszy 
#    (z góry na dół w skrypcie)