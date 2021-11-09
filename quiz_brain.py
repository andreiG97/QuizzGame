class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list

    def question_display(self):
        score = 0
        while self.q_number < len(self.q_list):
            current = self.q_list[self.q_number]
            self.q_number += 1
            q = input(f"Q.{self.q_number} " + current.text + 'True/False\n')
            if q.lower() == current.answer.lower():
                score += 1
                print(f"You are right.\n Your score is {score}/{self.q_number}")
            else:
                print(f"You are wrong.\n Your score is {score}/{self.q_number}")

