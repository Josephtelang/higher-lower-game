from flask import Flask
import random
app = Flask(__name__)

random_num = random.randint(0,9)
print(random_num)



@app.route("/")
def home():
    return "<h1>Guess the number between 0 and 9</h1>"\
            "<img Src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' >"
    
@app.route("/<int:guess>")
def guess_number(guess):

    if guess < random_num :
        return f"<h1 style = 'color : blue'>{guess} is to low</h1>"\
                "<img = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif >" 
    elif guess > random_num :
        return f"<h1 style = 'color : red'>{guess} is to high</h1>"\
                "<img = //media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif >"
    else:
        return f"<h1>It's {9} .You got it</h1>"\
                "<img = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif >"
    
if __name__ == "__main__":
    app.run(debug=True)