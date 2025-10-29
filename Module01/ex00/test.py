import recipe

def check_recipe(Pancake):
    if Pancake.name == "" or Pancake.name != str:
        print("Error in name\nPut correct name for the recipe")
        return
    if Pancake.cooking_lvl < 0 or Pancake.cooking_lvl > 5 or Pancake.cooking_lvl.isdigit() == False:
        print("Error in cooking_lvl\nPut level from 0 to 5")
        return
    if Pancake.cooking_time < 0 or Pancake.cooking_time.isdigit() == False:
        print("Error in cooking_time")

def main():
    Pancake = recipe.Recipe()
    Pancake.name = "Pancake"
    Pancake.cooking_lvl = 3
    Pancake.cooking_time = 20
    Pancake.ingredients = {"milk", "eggs", "flour"}
    Pancake.description = "Put it together on the frying pan"
    Pancake.recipe_type = "dessert"

    status = check_recipe(Pancake)

    Soup = recipe.Recipe()
    Soup.name = "Soup"

    print(Pancake.name)
    print(Soup.name)

if __name__=="__main__":
    main()
