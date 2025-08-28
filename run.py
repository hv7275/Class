from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    return Response('Hi, Khushi')
    
app.run(debug=True)

