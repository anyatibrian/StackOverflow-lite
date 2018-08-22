from flask import Flask, request, jsonify, make_response
from .models import questions
from .models import answers

# register the application name
app = Flask(__name__)

# access method of the class Questions
questions = questions.question_list()
# access method of the class Answers
answers = answers.answer_list()


@app.route('/')
def index():
    '''default home page'''
    return "Hello flask api endpoints"


def _get_question(question_id):
    '''
    protected method that returns the question
    Args:
        param (int): question_id
    Returns:
        question
    '''
    return next((question for question in questions
                if question['question_id'] == question_id), None)


def _get_answer_question(question_id):
    '''
    protected method that returns the answer
    Args:
        param (int): question_id
    Returns:
        answers
    '''
    if _get_question is False:
        return make_response(jsonify({'error': 'Question Not Found'}), 404)
    find_answer = []
    for answer in answers:
        if answer['question_id'] == question_id:
            find_answer.append(answer)
    return find_answer


def _find_question(question_title):
    '''
    protected method that returns the question
    Args:
        param (question_title): Question title
    Returns:
        question_title
    '''
    return next(filter(lambda q: q['question_title'] == question_title,
                questions), None)


def _answer_exist(answer_body):
    '''
    protected method that returns the answer
    Args:
        param (answer_body): answer body
    Returns:
        question_body
    '''
    return next(filter(lambda a: a['answer_body'] == answer_body,
                answers), None)


def _check_datatype(question_title, question_body, question_tag):
    if not isinstance(question_title, str) or \
     not isinstance(question_body, str) or \
     not isinstance(question_tag, str):
        return True


def _check_whitespace(question_title, question_body, question_tag):
    if question_title.isspace() or question_body.isspace() \
       or question_tag.isspace():
        return True
    if len(question_title) < 10 or len(question_body) < 10 \
       or len(question_tag) < 2:
        return True


def _check_answer_length(answer_body):
    if len(answer_body) < 10:
        return True


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
    '''Returns specific question given id'''
    question = _get_question(question_id)
    if not question:
        return make_response(jsonify({'error': 'Question Not Found'}), 404)
    return jsonify({
        'question': question,
        'answers': _get_answer_question(question_id)
        }), 200


@app.route('/api/v1/questions', methods=['POST'])
def ask_question():
    '''Creates question from request object (from user)'''
    if not request.json or 'question_title' not in request.json \
            or 'question_body' not in request.json \
            or 'question_tag' not in request.json:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

    last_qid = 0
    if len(questions) > 0:
        last_qid = questions[-1].get('question_id')

    question_id = last_qid + 1
    question_title = request.json.get('question_title')
    question_body = request.json.get('question_body')
    question_tag = request.json.get('question_tag')

    if _check_datatype(question_title, question_body, question_tag):
        return make_response(jsonify({'error': 'Bad Request'}), 400)
    if _check_whitespace(question_title, question_body, question_tag):
        return make_response(jsonify({'message': 'whitespace or empty'}),
                             501)
    if _find_question(question_title) is not None:
        return make_response(jsonify({'error': 'Question Already Created'}),
                             409)

    question = {'question_id': question_id, 'question_title': question_title,
                'question_body': question_body, 'question_tag': question_tag}
    questions.append(question)
    return jsonify({'question': question}), 200


@app.route('/api/v1/questions/<int:question_id>/answers', methods=['POST'])
def add_answer(question_id):
    if not request.json or 'answer_body' not in request.json:
        return make_response(jsonify({'error': 'Bad Request'}), 400)

    question = _get_question(question_id)
    if not question:
        return make_response(jsonify({'error': 'Question Not Found'}), 404)

    last_id = 0
    try:
        if len(answers) > 0:
            last_id = answers[-1].get('answer_id')

        answer_id = last_id + 1
        question_id = _get_question(question_id)['question_id']
        answer_body = request.json.get('answer_body')

        if _answer_exist(answer_body) is not None:
            return make_response(jsonify({"answer exist": answer_body}), 409)

        answer_length = _check_answer_length(answer_body)
        if not answer_length:
            answer = {
                'answer_id': answer_id,
                'question_id': question_id,
                'answer_body': answer_body
            }

        answers.append(answer)
        return jsonify({'answer': answer}), 201

    except:
        return jsonify({"message": "answer must be 10+ characters"})
    
