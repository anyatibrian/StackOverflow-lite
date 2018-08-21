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
        self.questions = []

        return self.questions

    def __str__(self):
        '''Returns string representation of the list'''
        return str(self.question_list)


class Answers:
    '''models class to hold the non persistent answers'''
    def answer_list(self):
        self.answers = []

        return self.answers

# Instantiate object of the classes
questions = Questions()
answers = Answers()


