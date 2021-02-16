from sys import argv

script, first, second, third = argv

print("This script is called:", script)
print("First variable is:", first)
print("Second var is called:", second)
print("Third one is called:", third)

# Uruchomić to z poleceniem "python ex13.py {nazwa_pierwszej} {nazwa_drugiej} {nazwa_trzeciej}", podając zamiast klamr nazwy zmiennych.
# To jest swego rodzaju nowością, nie używałem wcześniej argvs - chociaż miałem styczność z nadpisywaniem "opcji" uruchamiania programu z klawiatury,
# tj. np. "-o -a -i -l --LOGLEVEL", etc.