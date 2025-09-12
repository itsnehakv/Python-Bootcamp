from flask import Flask, render_template
import random

random_number = random.randint(0, 9)
print(random_number)

app= Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcm0xc3F4a3dobjk3c2V6d2M5Y3l2ZXVocHhnd3MyNzZmNnM2eXJ5YiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cRHgphdnVZMtRLZlT1/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjViMGR4cTBiYzdlcmI4a3k5bW5ubXJheG9lbzN0Z3U0YTltY2pwbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fQoIDlLW6A6BAhyev8/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2I2czVqb204NThjbjh5dXBhbDhweTRybWdrdnAyYXpsb25idnFxNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9xijGdDIMovchalhxN/giphy.gif'/>"
    else:
        return "<h1 style='color: green; text-align: center'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamplcTFsYzBsdG5sdXFtNG8yYXMxbm42djM2b29qb3NldjliYThpdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8DY8oKlTQyYCKanxT8/giphy.gif'/>"

if __name__=="__main__":
    app.run(debug=True)