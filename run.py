from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    context = [
        {
            'title': 'About Us',
            'content': 'This is the about page.'
        },
        {
            'title':'Harsh',
            'content':"Harsh Khushi"
        }
    ]
    return render_template('about.html', rams=context)

app.run(debug=True)

