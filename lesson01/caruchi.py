from inputroutines import intInRange, floatInRange
from food import FoodItem

def inputWithPrompt(type, lower, upper, prompt):
    print(prompt, end=' ')
    if type == int:
        return intInRange(lower, upper)
    if type == float:
        return floatInRange(lower, upper)

if __name__ == "__main__":
    FoodEntry = FoodItem(
        input("Enter food item's name: "),
        inputWithPrompt(int, 0, 500, "Enter the serving size in grams (or mL for liquids):"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of fat per serving:"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of carbs per serving:"),
        inputWithPrompt(float, 0.00, 50.00, "Enter the grams of protein per serving:"),
    )
    print("Nutritional information per serving of", FoodEntry.getName())
    print("Serving Size:", FoodEntry.getServingSize(), "grams / mL")
    print("Fat:", format(FoodEntry.getFat(), ".2f"), "grams")
    print("Carbohydrates:", format(FoodEntry.getCarbs(), ".2f"), "grams")
    print("Protein:", format(FoodEntry.getProtein(), ".2f"), "grams")
    print("Number of calories for 1 serving:", format(FoodEntry.calculateCalories(1), ".2f"))
    servings = inputWithPrompt(int, 0, 10, "\nEnter the number of servings consumed:")
    print("Number of calories for", servings, "serving(s):", format(FoodEntry.calculateCalories(servings), ".2f"))