from flask import Flask

# register the application name
app = Flask(__name__)


@app.route('/')
def index():
    '''default home page'''
    return "Hello flask api endpoints"
