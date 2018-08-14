from flask import Flask, request, jsonify, make_response, abort
from .models import questions

# register the application name
app = Flask(__name__)

# access method of the class Question
questions = questions.question_list()


@app.route('/')
def index():
    '''default home page'''
    return "Hello flask api endpoints"


def _get_question(question_id):
    '''
    protected method that returns id
    Args:
        param (int): question_id
    Returns:
        id
    '''
    return[question for question in questions
           if question['question_id'] == question_id]


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


@app.errorhandler(409)
def bad_request(error):
    '''
    Conflicting request, question exist
    Args:
        param (error): error
    Returns:
        conflicts, 409
    '''
    return make_response(jsonify({'error': 'Question Already Created'}), 409)


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    '''
    fetch all questions from the model
    Args:
        None
    Returns:
        questions, ok
    '''
    return jsonify({'questions': questions}), 200


@app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    '''
    Returns specific question given id
    Args:
        param (int): question id
    Returns:
        question, ok
    '''
    question = _get_question(question_id)
    if not question:
        abort(404)
    return jsonify({'question': question}), 200


@app.route('/api/v1/questions', methods=['POST'])
def ask_question():
    '''
    Creates question from request object (from user)
    Args:
        None
    Returns:
        created, 201
    '''
    if not request.json or 'question_class' not in request.json \
            or 'question_name' not in request.json:
        abort(400)

    question_id = questions[-1].get('question_id') + 1
    question_class = request.json.get('question_class')
    question_name = request.json.get('question_name')

    asked_question = _find_question(question_name)
    if asked_question is not None:
        abort(409)

    question = {
        'question_id': question_id,
        'question_class': question_class,
        'question_name': question_name,
        'answer': []
    }

    questions.append(question)
    return jsonify({'question': question}), 201


