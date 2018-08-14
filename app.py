from flask import Flask

# register the application name
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello flask api"


if __name__ == '__main__':
    app.run(debug=True)
