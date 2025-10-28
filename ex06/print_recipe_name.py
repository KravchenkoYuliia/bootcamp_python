import recipe

def print_recipe_names():
    
    print("\033[5m" + "ALL RECIPES IN THE COOKBOOK:\n", "\033[25m")
    
    index = 1
    for meal in recipe.cookbook:
        print(str(index) + ".", meal)
        index += 1
    print("")
