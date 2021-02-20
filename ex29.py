people = 20
cats = 30
dogs = 15

if people < cats:
    print("Zbyt dużo kotów! Świat jest skazany na zagładę!")

if people > cats:
    print("Nie za dużo kotów! Świat jest ocalony!")

if people < dogs:
    print("Świat się ślini!")

if people > dogs:
    print("Świat jest suchy!")

dogs += 5

if people >= dogs:
    print("Liczba ludzi jest większa lub równa liczbie psów.")

if people <= dogs:
    print("Liczba ludzi jest mniejsza lub równa liczbie psów.")

if people == dogs:
    print("Ludzie są psami.")

# 1. if to instrukcja warunkowa, która rozpatruje czy warunek jest prawdą czy fałszem. Jeśli warunek jest spełniony (prawdziwy), wykonuje wcięty blok.
#    Jeśli nie -> skrypt pomija wcięty blok i przechodzi dalej.
# 2. Wcięcie to sygnał rozpoczęcia bloku kodu, z którym interpreter ma się obejść w szczególny sposób, tj. w tym przypadku wykonać go warunkowo.
# 3. Jeśli kod nie jest wcięty to najprawdopodobniej otrzymamy błąd "Indentation Error", kompilator ma zakodowane, że po if-ie musi być wcięty blok.
# 4. Tak
# 5. Wszystkie powyższe instrukcje porównują wartości, więc jeśli je zmienimy, możemy zmienić wynik - wejdziemy w inny warunek.