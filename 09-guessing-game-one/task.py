import random

gen_number = random.randint(1, 9)

print("--- " + (str(gen_number)) + " ---")

win = False

while not win:
    usr_number = int(input("Guess number from 1 to 9: "))

    if usr_number == gen_number:
        print("You guessed the correct number! ")
        win = True
    elif usr_number > gen_number:
        print("Too high")
    else:
        print("Too low")
