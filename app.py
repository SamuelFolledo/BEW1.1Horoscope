from random import choice, sample
from flask import Flask, request, render_template #for query string (1hr 8mins)

app = Flask(__name__)

compliments = ['awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']
horoscopes = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

@app.route('/compliment') #this decorator on top of the function makes it a route
def get_compliments(): #method that gives the user's name a compliment
    name = request.args.get('name') #extract a query string we inputted from the text box
    show_compliments = request.args.get('show_compliments') #contains the value (on/none) of the check_box
    # compliment = choice(compliments) #choose randomly from our compliments list

    num_compliments = int(request.args.get('num_compliments')) #grabs the value we have stored in num_compliments and convert it to integer
    compliments_to_show = sample(compliments, num_compliments) #choose a unique random elements from a population sequence or set
    # return f"Hello there, {name}! You are so {compliment}!" #f lets you put the string in a variable
    return render_template('compliments.html', 
                            name = name, 
                            show_compliments = show_compliments, 
                            compliments = compliments_to_show ) #render_template(template_name_or_list, **context) = renders a template from the template folder with the give context

@app.route("/horoscopes")
def get_horoscope():
    name = request.args.get('name') #extract a query string
    horoscope = choice(horoscopes) #choose randomly from our compliments list
    
    pass
    num_compliments = int(request.args.get('num_compliments'))
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, num_compliments)
    return f"Hello there, {name}! You are so {horoscope}!" #f lets you put the string in a variable



@app.route('/')
def index(): #Show the homepage and ask the user's name
    return render_template('index.html') #instead of returning a HTML form, we change our route to call the render_template function with the file containing our function 


if __name__ == "__main__": #__main__ at the bottom of the file is the entry point
    app.run(debug=True) #debug should only be True on development mode as this is unsafe

