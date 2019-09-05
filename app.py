from random import choice, sample
from flask import Flask, request, render_template #for query string (1hr 8mins)

app = Flask(__name__)

compliments = ["coolio", "smashing", "neato", "fantabulous"]

@app.route('/compliments') #this decorator on top of the function makes it a route
def get_compliments(): #method that gives the user's name a compliment
    name = request.args.get('name') #extract a query string
    compliment = choice(compliments) #choose randomly from our compliments list
    return f"Hello there, {name}! You are so {compliment}!" #f lets you put the string in a variable

@app.route('/')
def index(): #index is the default home page
    """Show the homepage and ask the user's name."""
    return """
        <form action= '/compliments'>
        What is your name?
        <input type = "text" name = "name"></input>
        </form>
    """

if __name__ == "__main__": #__main__ at the bottom of the file is the entry point
    app.run(debug=True) #debug should only be True on development mode as this is unsafe

