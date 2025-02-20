import random
def deal_card():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(deck)
    return card

def calculate_score(the_deck):
    if sum(the_deck)==21 and len(the_deck)==2:
        return 0
    elif sum(the_deck)>21 and 11 in the_deck:
        the_deck.remove(11)
        the_deck.append(1)
    return sum(the_deck)

def compare(dealer_score,user_score):
    if user_score==dealer_score:
        print(" It is a tie!")
    elif dealer_score == 0:
        print(("You WONN"))
    elif user_score==0:
        print(("You WONN with a blackjack!"))
    elif dealer_score>21:
        print("Dealer went over. You win")
    elif user_score>21:
        print("You went over. You lose")
    elif user_score>dealer_score:
        print("You won!")
    elif user_score<dealer_score:
        print("You Lose")

def blackjack():
    user_cards=[]
    dealer_cards=[]
    game_over=False
    user_score=-1  #because 0 == blackjack
    dealer_score = -1
    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    while not game_over:
        user_score=calculate_score(user_cards)
        dealer_score=calculate_score(dealer_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f"computr cards: {dealer_cards},current score: {dealer_score}")

        print(f"Computers first card: {dealer_cards[0]}")

        if user_score==0 or dealer_score==0 or user_score>21:
            game_over=True
        else:
            continue_play = input("Type 'y' to get another card, type 'n' to pass: \n ").lower()
            if continue_play == 'y':
                user_cards.append(deal_card())
            else:
                game_over=True

    while dealer_score!=0 and dealer_score<17:
        dealer_cards.append(deal_card())
        dealer_score=calculate_score(dealer_cards)


        """the user will keep taking cards as long as we say 'y' 
         AND as long as user_score is NOT 0 (blackjack) or user_score is NOT >21.
         Only after the user is done or we say no, will the dealer pull another card
         (if the conditions are satisfied)"""


    print(f"Your final hand: [{user_cards}],current score: {user_score}")
    print(f"Computers final hand: [{dealer_cards}], final score:{dealer_score}")
    print(compare(user_score,dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()

