# File:         questions.py
# Purpose:      A class system to offer getters, setters for varying quiz question types.
#               
#               The file starts with a Question class object to create the base structure.
#               You'll also find the types of Multiple Choice, Fill in the Blank, and Short Answer as well.
# Author:       Leah Keenwood
# Date:         April 28th, 2024
#
#
# Creating a Question class object to give all Question types a base structure.
class Question:

    # Defining the default values needed to make Question class' functions work.
    def __init__(self, prompt="", correctAnswer="", points=0):
        self.__prompt = prompt
        self.__correctAnswer = correctAnswer
        self.__points = points

    # Defining getters
    def getPrompt(self):
        return self.__prompt

    def getCorrectAnswer(self):
        return self.__correctAnswer

    def getPoints(self):
        return self.__points

    # Defining setters
    def setPrompt(self, prompt):
        self.__prompt = prompt

    def setCorrectAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer

    def setPoints(self, points):
        self.__points = points

    # This function is for the types to create their own.
    def displayForTest(self):
        pass
    
    # Ensuring all data types are being displayed properly.
    def __str__(self):
        return f"Prompt: {self.getPrompt()}\nCorrect Answer: {self.getCorrectAnswer()}\nPoints: {self.getPoints()}"


# Creating a reusable guard clause for use with multiple choice class.
def withinIndexRange(index: int, list: list) -> bool:
    return 0 <= index < len(list)

# Each subsequent class is to utilize the Question Class' functions along with their own specific classes.
# 
# Creating Multiple Choice class with Question as it's base.
class MultipleChoice(Question):

    # Initializing the values needed to make MultipleChoice functions work.
    def __init__(self, prompt, correctAnswer, points, choices):
        super().__init__(prompt, correctAnswer, points)
        self.__choices = choices

    # Defining Multiple Choice getters
    def getChoice(self, index: int):
        # If zero is less than or equal to the index parameter, and index is
        # less than the length of the current choice list.
        if withinIndexRange(index, self.__choices):
            return self.__choices[index]
        else:
            print("Please provide an integer.")

    # Defining Multiple Choice setters
    def addChoices(self, choice):
        self.__choices.append(choice)

    def updateChoice(self, index, newChoice):
        if withinIndexRange(index, self.__choices):
            self.__choices[index] = newChoice

    # Creating a display prompt with the question prompt and choices listed below.
    def displayForTest(self):
        # Setting the initial prompt to the top of the output.
        output = self.getPrompt()

        # For each choice within the list, append it to the output.
        for index in range(len(self.__choices)):
            choice = self.getChoice(index)
            output += f"\n{choice}"
        return output

    # Appending Choices to ensure the data values are showing up accordingly.
    def __str__(self):
        return super().__str__() + f"Choices: {self.__choices()}"

# Creating Short Answer class with Question as it's base.
class ShortAnswer(Question):

    # Initializing the values needed to make ShortAnswer functions work.
    def __init__(self, prompt, correctAnswer, points, length=None):
        super().__init__(prompt, correctAnswer, points)
        self.__length = length

    # Defining ShortAnswer getters
    def getLength(self):
        return self.__length

    # Defining ShortAnswer setters
    def setLength(self, length):
        self.__length = length

    # Creating a display prompt with the question prompt and listing the character limit.
    def displayForTest(self):
        return f"{self.getPrompt()} (up to {self.getLength()} characters)"

    # Appending Character Limit to ensure the data values are showing up accordingly.
    def __str__(self):
        return super().__str__() + f"\nCharacter limit: {self.getLength()}"

# Creating a Fill in the Blank class with Question as it's base.
class FillInTheBlank(Question):

    # Initializing the Question values only, as this class needs no other variables.
    def __init__(self, prompt, correctAnswer, points):
        super().__init__(prompt, correctAnswer, points)

    # Creating a display prompt with the ask to "Fill in the blank:" prior.
    def displayForTest(self):
        return f"Fill in the blank: \n{self.getPrompt()}"
    
    # No extra data to report for the str, relay the default.
    def __str__(self):
        return super().__str__()