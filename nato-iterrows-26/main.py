import pandas as p
nato_data=p.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary={row.letter:row.code for (index,row) in nato_data.iterrows()}

user_input=input("Enter your name :  ").upper()

user_nato=[nato_dictionary[letter] for letter in user_input]   #ONLY thing i couldn't do by myself. nato_dictionary[letter] gives "value/code" associated with the letter
print(", ".join(user_nato))


'''***cannot use nato_data.to_dict() to create nato_dictionary bcs it'll be like {"letters":{0:"A",1:"B"...***'''



#shorter version in just 2 lines!
nato_data=p.read_csv("nato_phonetic_alphabet.csv")
print([  nato_data.code[nato_data.letter == letter].item()     for letter in input('Enter a word: ').upper()])
