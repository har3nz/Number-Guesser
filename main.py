import random

min_value = 1
max_value = 100

def random_value():
    return random.randint(min_value, max_value)

result = random_value()
print("I chose a number between 1 and 100 (1 and 100 included) and I want you to guess the number")
print("You have 10 tries")

def user_input():
    try_count = 10

    while try_count > 0:
        user_guess = int(input("Guess: "))

        if user_guess == result:
            print("That's right! You guessed it.")
            won = input("Type anything to restart...")
            random_value()
            print("I chose a number between 1 and 100 (1 and 100 included) and I want you to guess the number")
            print("You have 10 tries")
            break
            
        elif user_guess < result:
            print("Go higher.")
            while try_count > 0:
                user_input()
        elif user_guess > result:
            print("Go lower.")
            while try_count > 0:
                user_input()
        try_count -= 1
        print("Tries left:", try_count)
        if try_count == 0:
            print("You ran out of tries restarting the game")
            random_value()
            print("I chose a number between 1 and 100 (1 and 100 included) and I want you to guess the number")
            print("You have 10 tries")
            break

user_input()