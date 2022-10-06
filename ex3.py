import random

random_number = random.randint(1, 100)
guess = int(input("Number: "))
while random_number != guess:
    if guess > random_number:
        print("Lower")
    else:
        print("Higher")
    guess = int(input("Number: "))

print("Well done!!!")
