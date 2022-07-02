class QuizBrain:
    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0

    def still_has_question(self):
        return self.question_num<len(self.question_list)

    def check_answer(self,user_ans, correct_ans):
        if user_ans.lower()== correct_ans.lower():
            self.score+=1
            print("Correct!!")
            print(f'Your score is: {self.score}/{len(self.question_list)}')
        else:
            print(f'Correct answer was:{correct_ans}')
            print(f'Your score is: {self.score}/{len(self.question_list)}')

    def next_question(self):
        current_item = self.question_list[self.question_num]
        print(f'Q.{self.question_num + 1} :{current_item.text}',end=" ")
        ans = input("(True/False)")
        self.check_answer(ans, current_item.answer)
        self.question_num+=1

    def result(self):
        print("QUIZ OVER!!")
        print(f'Your final score is {self.score}/{len(self.question_list)}')
