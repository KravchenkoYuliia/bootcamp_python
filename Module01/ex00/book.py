
class Book:

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
    
    def __get_recipe_by_name__(self, name):
        if name in self.recipes_list:
            return str(name)
        else:
            return None

    def __get_recipe_by_types__(self, recipe_type):
        if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert":
            return self.recipes_list[recipe_type]
        else:
            return None

