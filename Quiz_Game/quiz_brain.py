class QuizBrain:
    def __init__(self,lit):
        self.question_number=0
        self.question_list=lit
        self.score=0
    def still_has_questions(self):
        length=len(self.question_list)
        return length> self.question_number
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(ans,current_question.answer)
    def check_answer(self,uans,cans):
        if uans.lower()==cans.lower():
            self.score+=1
            print("You are right")

        else:
            print("You are Wrong")
        print(f"Correct answer is {cans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    def ending(self):
        print("You have Completed Quiz")
        print(f"Your Final Score is:{self.score}/{self.question_number} ")



