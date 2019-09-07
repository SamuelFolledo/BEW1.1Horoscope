from random import choice, sample
from flask import Flask, request, render_template #for query string (1hr 8mins)

app = Flask(__name__)


horoscopes = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

@app.route('/horoscope')
def get_horoscope():
    name = request.args.get('name') #extract a query string
    num_horoscopes = int(request.args.get('num_horoscopes')) #grabs number of horoscopes to show depending on the amount of selected via dropdown
    show_horoscopes = request.args.get('show_horoscopes')
    horoscopes_to_show = sample(horoscopes, num_horoscopes)
    sign = request.args.get('sign')
    return render_template('horoscopes.html',
                            name = name,
                            sign = sign,
                            show_horoscopes = show_horoscopes,
                            horoscopes = horoscopes_to_show ) #display our horoscopes.html


@app.route('/')
def index(): #Show the homepage and ask the user's name
    return render_template('index.html') #instead of returning a HTML form, we change our route to call the render_template function with the file containing our function 


if __name__ == "__main__": #__main__ at the bottom of the file is the entry point
    app.run(debug=True) #debug should only be True on development mode as this is unsafe

