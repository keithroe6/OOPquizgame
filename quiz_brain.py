
# Step 4. bring up question and ask user to answer the question
# All of quiz functionality will be in this file

# 4a. Create a class called QuizBrain
class QuizBrain:
    # 4b. Create constructor to initialize the necessary attributes: Question number and user score which will have default values and question list which will be passed into the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    # 4c. Create a method that retrieves the question form the question list (created in main.py)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # 4d. List start at 0 so to display the correct question number for the next step increase question number by one
        self.question_number += 1
        # 4e. Show the number, text and ask for the users answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False: )")

        # 8e. When advancing to the next question check the answer the user gave
        self.check_answer(user_answer, current_question.answer)

    # Step 7. Create a method that advances the questions after the user has answered
    def still_has_questions(self):
        # This method will return a Boolean
        return self.question_number < len(self.question_list)
    
    
    #step 8. Create a method that will check the answer that the user gives
    def check_answer(self, user_answer, correct_answer):
        # 8a. Create if/else statement that compares user and the correct answer, be sure to account for varying cases in user's answer
        if user_answer.lower().strip() == correct_answer.lower():
            # 8b. Increase the score by 1
            self.score += 1
            # 8c. Let the user know they are correct
            print("You got it right! Woooo ♥️ 👍") 
        # 8d. Create else statement for when the user gets the answer wrong
        else:
            print("Darn! Missed that one. 🤔")
        
        # 8f. Display the correct answer
        print(f"The correct answer was: {correct_answer}")
        # 8g. Display the users score out of how many questions have been asked
        print(f"Your current score is: {self.score} / {self.question_number}")
        print('\n\n')