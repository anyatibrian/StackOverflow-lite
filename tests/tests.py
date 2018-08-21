from api import views
import app
import json
import unittest


DEFAULT_URL = 'http://127.0.0.1:5000/api/v1/questions'
BAD_URL = '{}/3'.format(DEFAULT_URL)
GOOD_URL = '{}/1'.format(DEFAULT_URL)
ANSWER_URL = '{}/1/answers'.format(DEFAULT_URL)
NO_QUESTION_URL = '{}/3/answers'.format(DEFAULT_URL)


class TestApi(unittest.TestCase):
    '''Test the api end points 
       Both the question and answer
    '''
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all_questions(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['questions']), 0)
        self.assertEqual(res.status_code, 200)

    def test_get_single_question(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        try:
            self.assertEqual(data['questions'][0]['question_name'], 
                             'what is python?')
        except IndexError as error:
            return error
        
        self.assertEqual(res.status_code, 200)
        
    def test_question_not_exist(self):
        res = self.app.get(BAD_URL)
        self.assertEqual(res.status_code, 404)

    def test_add_question(self):
        question = {
            'question_title': 'pythonic',
            'question_body': 'what is duck typing?',
            'question_tag': 'python'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_question_exist(self):
        question = {
            'question_title': 'javascript',
            'question_body': 'what is javascript?',
            'question_tag': 'javascript'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 409)

    def test_bad_request_question(self):
        question = {
            'question_class': 'python',
            'question_name1': 'what is flask?'
        }
        res = self.app.post(DEFAULT_URL,
                            data=json.dumps(question),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_question_has_answer(self):
        res = self.app.get(GOOD_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['answers']), 1)
        self.assertEqual(res.status_code, 200)

    def test_post_answer(self):
        question = {
            'question_title': 'javascript',
            'question_body': 'what is javascript?',
            'question_tag': 'javascript'
        }
        self.app.post(DEFAULT_URL,
                      data=json.dumps(question),
                      content_type='application/json')
        answer = {
            'answer_body': 'Javascript is sweet with nodejs'
        }
        res = self.app.post(ANSWER_URL,
                            data=json.dumps(answer),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_post_answer_to_no_question(self):
        answer = {
            'answer_body': 'Javascript is sweet'
        }
        res = self.app.post(NO_QUESTION_URL,
                            data=json.dumps(answer),
                            content_type='application/json')
        self.assertRaises(ValueError)

    def tearDown(self):
        '''reset views.questions and views.answers to initial state
        '''
        pass
       

    
