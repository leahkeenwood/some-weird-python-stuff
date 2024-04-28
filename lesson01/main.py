# File: main.py
# Purpose:      Provide a Command Line utility to present your nutritional information.
#               Using this, will create an auto-filled summary of the food, it's fat, 
#               carbs, & protein, how many serving sizes it has, and even provides the calorie
#               count of a single serving, or more if you provide a number of them.
# Author:       Leah Vessell
# Date:         April 6th, 2024

# Importing necessary functions into main.py from food.py and inputroutines.py
# FoodItem allows the code to have an array of sorts to store all the gathered data.
# intInRange & floatInRange gives user prompts for a floating point or an integer.
from food import FoodItem
from inputroutines import intInRange, floatInRange

# Adding string prompt to intInRange & floatInRange to clean up code.
# You can specify an int or float, depending on what's needed.
# A string parameter was added to give the user a reference on what to add.
def inputWithPrompt(type, lower, upper, prompt):
    print(prompt, end=' ')
    if type == int:
        return intInRange(lower, upper)
    if type == float:
        return floatInRange(lower, upper)

# Now it's time to run the actual code.
if __name__ == "__main__":

    # We'll start by using our newly created function to ask the user for:
    # Name, Serving Size, and Fat, Carbs & Protein per Serving.
    FoodEntry = FoodItem(
        input("Enter food item's name: "),
        inputWithPrompt(int, 0, 500, "Enter the serving size in grams (or mL for liquids):"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of fat per serving:"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of carbs per serving:"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of protein per serving:"),
    )
    # Display nutritional information per serving
    summary = """
    Nutritional information per serving of {name}
    Serving Size: {size} grams / mL
    Fat: {fat} grams
    Carbohydrates: {carbs} grams
    Protein: {protein} grams
    Number of calories for 1 serving: {servings}
    """.format(
        name = FoodEntry.getName(), 
        size = FoodEntry.getServingSize(),
        fat = (FoodEntry.getFat(), ".2f"),
        carbs = (FoodEntry.getCarbs(), ".2f"),
        protein = format(FoodEntry.getProtein(), ".2f"),
        servings = format(FoodEntry.calculateCalories(1), ".2f")
        )

    # Input number of servings consumed
    ConsumedServings = inputWithPrompt(int, 0, 10, "\nEnter the number of servings consumed:")

    # Calculate total calories consumed
    print("Number of calories for", ConsumedServings, "serving(s):", format(FoodEntry.calculateCalories(ConsumedServings), ".2f"))