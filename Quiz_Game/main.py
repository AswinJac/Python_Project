from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import art
print(art.intro)
question_bank=[]
for i in question_data:
    question=Question(i["question"],i["correct_answer"])
    question_bank.append(question)
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.ending()
print(art.end)