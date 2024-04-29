# File:         main.py
# Purpose:      A CLI Utility to ask questions and answer them accordingly.
#               These have a grading too, tallying up points to your goal.
#
#               The majority of this program relies on the questions.py file.
# Author:       Leah Keenwood
# Date:         April 28th, 2024
#
# We'll start by importing our classes from questions.py
from questions import MultipleChoice, ShortAnswer, FillInTheBlank

# Functions for User's Input.
#
# answerQuestion's purpose is to provide the question, depending on the quiz type.
def answerQuestion(question):
   # Creating a global variable for main script
   global answer

   # First providing the question, before asking the user to provide an answer.
   # The answer is then stored in the global answer variable.
   print(quiz[question].displayForTest())
   answer = input("\nEnter your answer: ")
   return

# gradeQuestion takes the answerQuestion's answer and checks if the answer is correct.
# The function then provides points to the user.
def gradeQuestion(question, userAnswer):
   # Setting points as a global value.
   global points

   # These vaiables will take the correct answer and user answer converting it to lowercase.
   # If the question is Multiple Choice, it splits the answer accordingly.
   correctAnswerLowercase = quiz[question].getCorrectAnswer().lower().split(". ")
   userAnswerLowercase = userAnswer.lower()

   # With the new variables, we can check if the user answer applies to the correct answer.
   # If Multiple choice, this can be "a", "A", or "Dragon", and you'll still get an accurate result.
   if userAnswerLowercase not in correctAnswerLowercase:
      print(f"Incorrect... The answer is {quiz[question].getCorrectAnswer()}.\n")
   else:
      # This function can tally up the points, offering the points you received, and how many total points you have overall.
      points += quiz[question].getPoints()
      print(f"\nYou earned {quiz[question].getPoints()} points! \nYou now have {points} points.\n")

# This is the actual script itself.
if __name__ == "__main__":
   # We reset the points to 0, also giving the points variable a starting value for gradeQuestion to work.
   points = 0

   # We set up the quiz into a list, using each item as a question.
   quiz = [
      MultipleChoice("Which animal is the Drexel mascot?", "a. Dragon", 10, ["a. Dragon", "b. Tiger", "c. Bulldog"]),
      FillInTheBlank("The name of Drexel University's founder is ____ J. Drexel.", "Anthony", 10),
   ]

   # In doing a list for the questions, we can do a for loop to go through each question, making our code cleaner overall.
   for index in range(len(quiz)):
      answerQuestion(index)
      gradeQuestion(index, answer)