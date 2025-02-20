import random
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

lives = 6


# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)

game_over = False
guessed_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"HEY!you have already guessed {guess} :)")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
