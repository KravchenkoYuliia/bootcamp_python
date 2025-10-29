
class Recipe:
    
    def __init__(self, name, lvl, time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __check_recipe__(self):
        try:
            self._check_name_()
            self._check_lvl_()
            self._check_cooking_time_()
            self._check_ingredients_()
            self._check_description_()
            self._check_recipe_type_()
        except:
            raise
    
    def __str__(self):
        recipe = f"The recipe of {self.name}:) \n\nCooking level = {self.cooking_lvl}/5\nEstimated time of cooking = {self.cooking_time} minutes\nAll you need is: {', '.join(elem for elem in self.ingredients)}"
        if self.description != "":
            recipe += f"\nAbout {self.name}: {self.description}"
        recipe += f"\nType: {self.recipe_type}"

        return recipe

    def __check_string__(self, data_to_check):
        if (str(data_to_check,).isdigit()
            or str(data_to_check,) == ""
            or str(data_to_check,).isspace()
            or not str(data_to_check,).strip().isprintable()
            ):

            raise


    def _check_name_(self):
        try:
            str(self.name)
            self.__check_string__(self.name)
        except:
            print("Invalid name for the recipe")
            raise Exception("Invalid name for the recipe")



    def _check_lvl_(self):
         try:
             int(self.cooking_lvl)
         except:
            print("Invalid cooking level")
            raise Exception("Invalid cooking level")
        
         if int(self.cooking_lvl) < 1 or int(self.cooking_lvl) > 5:
            print("Invalid cooking level")
            raise Exception("Invalid cooking level")
            
    
    def _check_cooking_time_(self):
        try:
            int(self.cooking_time)
        except:
            print("Invalid cooking time")
            raise Exception("Invalid cooking time")
        if int(self.cooking_time) < 1 or int(self.cooking_time) > 1000:
            print("Invalid cooking time")
            raise Exception("Invalid cooking time")
    
    def _check_ingredients_(self):
        
        for elem in self.ingredients:
            try:
                self.__check_string__(elem)
                str(elem)
            except:
                print("Invalid ingredients")
                raise Exception("Invalid ingredients")
    

    def _check_description_(self):
        try:
            str(self.description)
        except:
            print("Invalid description")
            raise Exception("Invalid description")
           
        if (str(self.description).isdigit()
            or str(self.description).isspace()
            or not str(self.description).strip().isprintable()
            ):

            print("Invalid description")
            raise Exception("Invalid description")
    

    def _check_recipe_type_(self):
        try:
            str(self.recipe_type)
        except:
            print("Invalid recipe type\nPut [starter], [lunch] or [dessert]")
            raise Exception("Invalid recipe type")
        
        if (self.recipe_type != "starter"
                and self.recipe_type != "lunch"
                and self.recipe_type != "dessert"
                ):

            print("Invalid recipe type\nPut [starter], [lunch] or [dessert]")
            raise Exception("Invalid recipe type")

