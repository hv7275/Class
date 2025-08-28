from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '<h1 style="color:aqua">Hello Word!, Hi Khushi</h1>'

app.run(debug=True)