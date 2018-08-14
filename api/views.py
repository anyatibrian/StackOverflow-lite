from flask import Flask, request, jsonify, make_response, abort
from .models import Questions

# register the application name
app = Flask(__name__)
# instantiates questions object
questionsObj = Questions()
questions = questionsObj.question_list()


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


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    '''
    fetch all questions from the model
    Args:
        None
    Returns:
        questions
    '''
    return jsonify({'questions': questions}), 200


@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_question(id):
    '''
    Returns specific question given id
    Args:
        param (int): question id
    Returns:
        question
    '''
    question = _get_question(id)
    if not question:
        abort(404)
    return jsonify({'question': question}), 200


