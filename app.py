from random import choice, sample
from flask import Flask, request, render_template #for query string (1hr 8mins)

app = Flask(__name__)

compliments = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']
horoscopes = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

@app.route('/compliment') #this decorator on top of the function makes it a route
def get_compliments(): #method that gives the user's name a compliment
    name = request.args.get('name') #extract a query string
    show_compliments = request.args.get('show_compliments') #extract a query string that has a key "show_compliments"
    compliment = choice(compliments) #choose randomly from our compliments list

    # num_compliments = int(request.args.get('num_compliments'))
    # compliments_to_show = sample(compliments, num_compliments)
    return f"Hello there, {name}! You are so {compliment}!" #f lets you put the string in a variable

@app.route("/horoscopes")
def get_horoscope():
    name = request.args.get('name') #extract a query string
    horoscope = choice(horoscopes) #choose randomly from our compliments list
    
    pass
    num_compliments = int(request.args.get('num_compliments'))
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, num_compliments)
    return f"Hello there, {name}! You are so {compliment}!" #f lets you put the string in a variable



@app.route('/')
def index(): #Show the homepage and ask the user's name
    return render_template('index.html') #instead of returning a HTML form, we change our route to call the render_template function with the file containing our function 
    
    """
        <form action= '/compliments'>
        What is your name?
        <input type = "text" name = "name"></input>
        </form>
    """

if __name__ == "__main__": #__main__ at the bottom of the file is the entry point
    app.run(debug=True) #debug should only be True on development mode as this is unsafe

