from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pavel'}
    posts = [
        {
            'author': {'username':'Pasha'},
            'body': 'Beautiful day in trash!'
        },
        {
            'author': {'username':'Матвей'},
            'body': 'Щас бы котлетку с пюрешкой.'
        },
        {
            'author': {'username':'Илья'},
            'body': 'Что делать-то?'
        }
    ]
    return render_template('index.html',title ='home', user = user,posts = posts)