from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

bank=[]
for i in range(0,len(question_data)):
    q=Question(question_data[i]["text"], question_data[i]["answer"])
    bank.append(q)

q=QuizBrain(bank)
while q.still_has_question():
    q.next_question()
q.result()
