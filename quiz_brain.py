class QuizBrian:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.is_correct = True

    def next_question(self):
        while self.is_correct:
            current_question = self.question_list[self.question_number]
            answer = input(f"Q. {self.question_number + 1}: {current_question.text} (True/False): ")

            if answer == current_question.answer:
                self.score += 1
                self.question_number += 1
            else:
                self.is_correct = False

        
        
    