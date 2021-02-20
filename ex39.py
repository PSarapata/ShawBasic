# mapowanie (odwzorowanie) to kluczowa koncepcja w słowniku
from os import stat


states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francissco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

print('-' * 10)
print('Abbreviation for Michigan is: ', states['Michigan'])
print('Abbreviation for Florida is: ', states['Florida'])

print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'State {state} has the abbreviation of {abbrev}')

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'State {abbrev} has city: {city}')

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'State {state} has the abbreviation of {abbrev}')
    print(f'And the city: {cities[abbrev]}')

print('-' * 10)
state = states.get('Texas')

if not state:
    print("We're sorry, there is no state called Texas.")

city = cities.get('TX', 'Does not exist')
print(f'City for state "TX" is: {city}')
