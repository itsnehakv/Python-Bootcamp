import art
from game_data import data
import random

def printing_state(the_person):
    return f"{the_person["name"]},{the_person["description"]} from {the_person["country"]}"

def compare(guess,A,B):
    follower_count_A = A["follower_count"]
    follower_count_B = B["follower_count"]

    if follower_count_A>follower_count_B:
        return guess=='A'
    else:
        return guess=='B'


def higher_or_lower():
    print(art.logo)
    game_over=False
    score=0
    person2 = random.choice(data) #only for first iteration. other all person2 will be person1
    while not game_over:
        person1=person2
        person2 = random.choice(data)
        while person1==person2:
            person2=random.choice(data)
        print(f"Compare A: {printing_state(person1)}")
        print(art.vs)
        print(f"Against B: {printing_state(person2)}")
        choice = input("Who has more followers? Type 'A' or 'B': \n").upper()
        answer=compare(choice,person1,person2)


        if answer:
            score+=1
            print(f"You're right! Current score {score}")
        else:
            print("\n"*80)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


higher_or_lower()

