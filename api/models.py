class Questions:
    '''Model class to hold the non-persistent questions'''
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
                'question_id': 1,
                'question_class': 'python',
                'question_name': 'what is python?'    
            },
            {
                'question_id': 2,
                'question_class': 'javascript',
                'question_name': 'what is javascript?'
            }]

        return self.questions

    def __str__(self):
        '''Returns string representation of the list'''
        return str(self.question_list)


class Answers:
    '''models class to hold the non persistent answers'''
    def answer_list(self):
        self.answers = [
                        {'answer_id': 3,
                         'question_id': 1,
                         'answer_body': 'Python is an interpreted high-level \
                          programming language for \
                           general-purpose programming.'
                         },
                        {'answer_id': 2,
                         'question_id': 2,
                         'answer_body': 'Python is an interpreted high-level \
                          programming language for general-purpose \
                          programming.Created by Guido van Rossum and \
                          first released in 1991'
                         }]

        return self.answers

# Instantiate object of the classes
questions = Questions()
answers = Answers()


