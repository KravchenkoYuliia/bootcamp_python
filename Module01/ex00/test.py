import recipe
import book
import datetime

def main():
    
    Pancake = recipe.Recipe("Pancake", 3, 20, ["milk", "eggs"], "So tasty", "dessert")
    try:
        Pancake.__check_recipe__()
    except:
        return

    #print(str(Pancake))


    recipes_list = {
            "starter" : "Snack",
            "lunch"   : "Rice",
            "dessert" : "Pancake",
            }

    creation_date = datetime.datetime.now()
    last_update = datetime.datetime.now()
    First_book = book.Book("First_book", last_update, creation_date, recipes_list)


    result = First_book.__get_recipe_by_name__(Pancake)
    if result:
        print(result)
    
if __name__=="__main__":
    main()
