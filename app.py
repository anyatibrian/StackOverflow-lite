# local import
from api.views import app


if __name__ == '__main__':
    '''creates application runner (python script)'''
    app.run(debug=True)
