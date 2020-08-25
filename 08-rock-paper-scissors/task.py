import random

options = ["rock", "paper", "scissors"]


def display_options():
    print("Rock, " + "Paper, " + "Scissors, ")


def get_player_choice():
    choice = input("Your choice: ").lower()
    return choice


def get_computer_choice():
    choice = str(options[random.randint(0, 2)])
    return choice


def display_choices(player_choice, computer_choice):
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")


def display_results(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Draw ! 😐")
    elif player_choice == options[0] and computer_choice == options[2]:
        print("You won! 🎉")
    elif player_choice == options[1] and computer_choice == options[0]:
        print("You won! 🎉")
    elif player_choice == options[2] and computer_choice == options[1]:
        print("You won! 🎉")
    else:
        print("You loose 🙁")


def game():
    display_options()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    display_choices(player_choice, computer_choice)
    display_results(player_choice, computer_choice)


game()
