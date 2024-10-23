import data
import question_model
import quiz_brain

question_bank = []

for question in data.question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrian(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz. Well Done!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")