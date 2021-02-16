# Tak jak już wcześniej zauważyłem, ta książka odpowiada na sporo najczęstszych pytań zadawanych przez świeżaków.

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
avg_psgrs_pcar = passengers / cars_driven

print("Dostępnych jest", cars, "samochodów.")
print("Dostępnych jest tylko", drivers, "kierowców.")
print("Dziś będzie", cars_not_driven, "pustych samochodów.")
print("Dziś możemy przetransportować", int(carpool_capacity), "osób.")
print("Mamy dziś do przewiezienia", passengers, "pasażerów.")
print("Musimy umieścić średnio", int(avg_psgrs_pcar), "osoby w każdym samochodzie.")
