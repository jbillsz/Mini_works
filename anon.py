class AnonymousSurvey(object):
    """ Collect Anonymous answers to a survey question"""

    def __init__(self, question):
        # store a question and answers
        self.question = question
        self.answers = []

    def show_question(self):
        """ Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """ store new response"""
        self.answers.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Show survey results: ")
        for i in self.answers:
            print(f"- {i}")
