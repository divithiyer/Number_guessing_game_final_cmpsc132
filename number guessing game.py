<<<<<<< HEAD
import random

def play_game():
    print()
    print("Choose a difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        low = 1
        high = 50
    elif choice == "2":
        low = 1
        high = 100
    elif choice == "3":
        low = 1
        high = 200
    else:
        print("Invalid choice. Medium difficulty will be used.")
        low = 1
        high = 100

    secret_number = random.randint(low, high)
    guess = 0
    attempts = 0

    print()
    print("I have chosen a number between", low, "and", high)

    while guess != secret_number:
        user_input = input("Enter your guess: ")

        if user_input.isdigit():
            guess = int(user_input)

            if guess >= low and guess <= high:
                attempts = attempts + 1

                if guess < secret_number:
                    print("Too low")
                elif guess > secret_number:
                    print("Too high")
                else:
                    print("Correct! You guessed it in", attempts, "attempts.")
            else:
                print("Enter a number between", low, "and", high)
        else:
            print("Invalid input. Enter a whole number.")

def main():
    play_again = "yes"

    print("Welcome to the Number Guessing Game!")

    while play_again == "yes":
        play_game()
        print()
        play_again = input("Do you want to play again? Type yes or no: ")

    print("Thanks for playing!")

=======
import random

def play_game():
    print()
    print("Choose a difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        low = 1
        high = 50
    elif choice == "2":
        low = 1
        high = 100
    elif choice == "3":
        low = 1
        high = 200
    else:
        print("Invalid choice. Medium difficulty will be used.")
        low = 1
        high = 100

    secret_number = random.randint(low, high)
    guess = 0
    attempts = 0

    print()
    print("I have chosen a number between", low, "and", high)

    while guess != secret_number:
        user_input = input("Enter your guess: ")

        if user_input.isdigit():
            guess = int(user_input)

            if guess >= low and guess <= high:
                attempts = attempts + 1

                if guess < secret_number:
                    print("Too low")
                elif guess > secret_number:
                    print("Too high")
                else:
                    print("Correct! You guessed it in", attempts, "attempts.")
            else:
                print("Enter a number between", low, "and", high)
        else:
            print("Invalid input. Enter a whole number.")

def main():
    play_again = "yes"

    print("Welcome to the Number Guessing Game!")

    while play_again == "yes":
        play_game()
        print()
        play_again = input("Do you want to play again? Type yes or no: ")

    print("Thanks for playing!")

>>>>>>> b63b6ce4822a1460630dca9254784cd9c33eb5a0
main()