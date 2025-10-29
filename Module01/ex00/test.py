import recipe

def main():
    
    Pancake = recipe.Recipe("Pancake", 3, 20, ["milk", "eggs"], "So tasty", "dessert")
    try:
        Pancake.__check_recipe__()
    except:
        return

    print(str(Pancake))

if __name__=="__main__":
    main()
