class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list

    def question_display(self):
        flag = True
        while flag:
            current = self.q_list[self.q_number]
            q = input(f"Q.{self.q_number + 1} " + current.text + 'True/False\n')
            if q == current.answer:
                self.q_number += 1
            else:
                flag = False
