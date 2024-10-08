# remove warning:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# pip install waitress
# git init
# git add .
# git commit -m "python flask tutorial"
# if you have set up git repository, use these
# git remote add origin https://github.com/ipraisethelord/python-weather.git
# git branch -M main
# git push -u origin main
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
# import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
     # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city ="Sacramento"
    weather_data = get_current_weather(city)
    # city i snot found by API
    if not weather_data['cod'] == 200:
        return render_template('city_not_found.html')
    
    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )



if __name__=="__main__":
    app.run()
#     # for error using debug mode
#     # os.environ['FLASK_ENV'] = 'development'
#     serve(app, host="0.0.0.0", port=8000)