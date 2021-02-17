def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You got {cheese_count} cheese pieces...")
    print(f"You got {boxes_of_crackers} boxes of crackers!")
    print("It's enough to throw a party!\n")

print("We can simply pass numbers to our function:")
cheese_and_crackers(20, 30)

print("Or we can use script variables")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can also perform arithmetic operations inside our function!")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two!")
cheese_and_crackers(amount_of_cheese + 10, 20 + amount_of_crackers)
