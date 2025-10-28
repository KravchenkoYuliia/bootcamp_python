import recipe

def choose_recipe_name():

    stop = False
    while stop == False:
       
        print("\033[45m" + "CHOOSE YOUR RECIPE" + "\033[0m")
        print("If you want to SKIP this: press [Enter]")
        recipe_name = input("Print here: ")
        if recipe_name == "":
            return 
        print("")
        

        if recipe_name in recipe.cookbook:
            print("\033[4m" + "Ingredients:" + "\033[0m")
            for ingredient in recipe.cookbook[recipe_name]["ingredients"]:
                print(ingredient)
            print("")
            print("\033[4m" + "Meal:" + "\033[0m" + "\n" + recipe.cookbook[recipe_name]["meal"])
            print("")
            print("\033[4m" + "Preparation time:" + "\033[0m" + "\n" + recipe.cookbook[recipe_name]["prep_time"])
            stop = True
        else:
            print("There is no such recipe")
