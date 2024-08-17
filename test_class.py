import unittest
from anon import AnonymousSurvey

class test_survey(unittest.TestCase):

    def test_response(self):
        question = "What language did you first learn to speak."
        my_survey= AnonymousSurvey(question)

        language = "French"
        response = my_survey.store_response(language)
        self.assertIn(language, my_survey.answers)

    def multi_response(self):
        question = "What language did you first learn to speak."
        my_survey= AnonymousSurvey(question)

        language = ["French", "English","Twi"]
        for dialect in language:
            self.assertIn(dialect, my_survey.answers)
unittest.main()
