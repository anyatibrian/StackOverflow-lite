class Questions:
    '''Model class to hold the non-persistent code'''
    def question_list(self):
        '''
        Intializes questions
        Args:
            None
        Returns:
            questions
        '''
        self.questions = [
            {
                'id': 1,
                'question_class': 'python',
                'question_name': 'what is python?',
                'answer': [
                    {'answer_id': 1,
                     'answer_body': 'Python is an interpreted high-level \
                        programming language for general-purpose programming.'
                     },
                    {'answer_id': 2,
                     'answer_body': 'Python is an interpreted high-level \
                        programming language for general-purpose programming.\
                        Created by Guido van Rossum and first released in 1991'
                     }]
            },
            {
                'id': 2,
                'question_class': 'javascript',
                'question_name': 'what is javascript?',
                'answer': [
                    {'answer_id': '',
                     'answer_body': ''
                     }
                    ]
            }]

        return self.questions

    def __str__(self):
        '''Returns string representation of the list'''
        return str(self.question_list)


