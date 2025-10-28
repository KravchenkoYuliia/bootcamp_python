import recipe

def add_new_recipe():
    
    print("\n" + "\033[45m"
            + "NOW YOU CAN ADD YOUR OWN RECIPE" + "\033[0m")
    name = input("\033[4mEnter a name: \033[0m")
    
    ingredient = "Smth"
    ingredients = []

    while 1:

        ingredient = input("\033[4mEnter ingredients: \033[0m")
        if ingredient == "":
            print("")
            break
        ingredients.append(ingredient)
    
    meal_type = input("\033[4mEnter a meal type: \033[0m")
    time = input("\033[4mEnter a preparation time: \033[0m")

    recipe.cookbook[name] = {"ingredients" : ingredients, "meal" : meal_type, "prep_time" : time}
