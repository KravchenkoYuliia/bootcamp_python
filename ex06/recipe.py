cookbook = {
            "Sandwich": {
                    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
                    "meal"       : "lunch",
                    "prep_time"  : "10",
                    },
            "Cake": {
                    "ingredients": ["flour", "sugar", "eggs"],
                    "meal"       : "dessert",
                    "prep_time"  : "60",
                    },
            "Salad": {     
                    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
                    "meal"       : "lunch",
                    "prep_time"  : "15",
                    },
            }

def print_recipe_names():
    
    print("\033[5m" + "All recipes in the cookbook:\n", "\033[25m")
    
    index = 1
    for meal in cookbook:
        print(str(index) + ".", meal)
        index += 1
    print("")

def choose_recipe_name():

    print("\033[45m" + "Choose one index" + "\033[0m")
    recipe = input("")
    print("")

    if recipe == "1":
        recipe_name = "Sandwich"
    elif recipe == "2":
        recipe_name = "Cake"
    elif recipe == "3":
        recipe_name = "Salad"
    else:
        print("Invalid index")
        return

    print("\033[4m" + "Ingredients:" + "\033[0m")
    for ingredient in cookbook[recipe_name]["ingredients"]:
        print(ingredient)
    print("")
    print("\033[4m" + "Meal:" + "\033[0m" + "\n" + cookbook[recipe_name]["meal"])
    print("")
    print("\033[4m" + "Preparation time:" + "\033[0m" + "\n" + cookbook[recipe_name]["prep_time"])



def main():
    print_recipe_names()
    choose_recipe_name()
    

if __name__=="__main__":
    main()
