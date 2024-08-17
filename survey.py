from anon import AnonymousSurvey

# Define a survey question:
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter q at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == "q":
        break

    my_survey.store_response(response.title())

print("\nThanks to everyone who participated in the survey.")
my_survey.show_results()
