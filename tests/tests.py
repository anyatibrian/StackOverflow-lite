from api import views, models
import app
from copy import deepcopy
import json
import unittest


DEFAULT_URL = 'http://127.0.0.1:5000/api/v1/questions'
BAD_URL = '{}/3'.format(DEFAULT_URL)
GOOD_URL = '{}/2'.format(DEFAULT_URL)


class TestApi(unittest.TestCase):
    '''Test the api end points'''
    def setUp(self):
        self.questionCopy = deepcopy(views.questions)
        self.answerCopy = deepcopy(views.answers)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all_questions(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(len(data['questions']), 2)
        self.assertEqual(res.status_code, 200)

    def test_get_single_question(self):
        res = self.app.get(DEFAULT_URL)
        data = json.loads(res.get_data())
        self.assertEqual(data['questions'][0]['question_name'], 
                         'what is python?')
        self.assertEqual(res.status_code, 200)
        
    def test_question_not_exist(self):
        res = self.app.get(BAD_URL)
        self.assertEqual(res.status_code, 404)

    def tearDown(self):
        '''reset views.questions and views.answers to initial state
        '''
        views.questions = self.questionCopy
        views.answers = self.answerCopy

    
