import print_recipe_name
import choose_recipe_name
import delete_recipe_name
import add_new_recipe
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

def main():

    print("Welcome to the Python Cookbook!\nList of available options:\n\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")

    while 1:
        choice = input("\nPlease select an option: ")

        if choice.isdigit() == False:
            print("Invalid option")
            print("List of available options:\n\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
        elif int(choice) == 1:
            add_new_recipe.add_new_recipe()
        elif int(choice) == 2:
            delete_recipe_name.delete_recipe_name()
        elif int(choice) == 3:
            choose_recipe_name.choose_recipe_name()
        elif int(choice) == 4:
            print_recipe_name.print_recipe_names()
        elif int(choice) == 5:
            print("By :)")
            return
        else:
            print("Invalid option")
            print("List of available options:\n\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")

if __name__=="__main__":
    main()
