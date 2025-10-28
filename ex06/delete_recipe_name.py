import recipe

def delete_recipe_name():
    
    print("\n" + "\033[45m"
            + "If you want to REMOVE A RECIPE         : write [recipe's name]"
            + "\033[0m" + "\n" + "\033[45m"
            + "If you want to REMOVE ALL the recipes  : write [all]"
            + "\033[0m"
            + "\033[0m" + "\n"
            + "If you want to SKIP this               : press [Enter]")
    stop = False
    while stop == False:
        recipe_name = input("Print here: ")
        
        if recipe_name == "":
            return
        elif recipe_name == "all":
            recipe.cookbook.clear()
        elif recipe_name in recipe.cookbook:
            recipe.cookbook.pop(recipe_name)
            stop = True
        else:
            print("There is no such recipe :(")
