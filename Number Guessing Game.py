import random
import art

def compare(guess,number):
    if guess == number:
        print(f"You guessed the correct number: {number}")
        return
    elif guess < number-20:
        print("Your guess is too low!")
    elif guess < number:
        print("Your guess is low!")
    elif guess > number + 20:
        print("Your guess is too high!")
    elif guess > number:
        print("Your guess is high!")

def number_guessing():
    number = random.randint(1, 100)
    print(art.logo)
    print("Guess a number between 1 and 100")
    mode=input("Choose a difficulty level:- easy or hard\n").lower()
    if mode=='hard':
        attempts=5
    else:
        attempts=10
    not_over=True
    guess=0
    while not_over:
        print(f"You have {attempts} guesses remaining")
        for guesses in range(1):
            guess=int(input("Make a guess:"))
            compare(guess,number)
        if guess!=number:
            print("Guess again")
            attempts-=1
            if attempts==0:
                not_over=False
                print("You have failed to guess the number. The number is ",number)
        else:
            return

number_guessing()






