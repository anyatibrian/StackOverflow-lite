from flask import Flask, request, jsonify, make_response
from .models import questions

# register the application name
app = Flask(__name__)


@app.route('/')
def index():
    '''default home page'''
    return "Hello flask api endpoints"


def _get_question(id):
    '''
    protected method that returns id
    Args:
        param (int): Question id
    Returns:
        id
    '''
    return[question for question in questions if question['id'] == id]


def _find_question(question_name):
    '''
    protected method that returns the question
    Args:
        param (question_name): Question name
    Returns:
        question_name
    '''
    return next(filter(lambda q: q['question_name'] == question_name,
                questions), None)


@app.errorhandler(404)
def not_found(error):
    '''
    Request Not Found
    Args:
        param (error): error
    Returns:
        404
    '''
    return make_response(jsonify({'error': 'Question Not Found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    '''
    Server fails to make a respond due to bad request
    Args:
        param (error): error
    Returns:
        400
    '''
    return make_response(jsonify({'error': 'Question Not Found'}), 400)


