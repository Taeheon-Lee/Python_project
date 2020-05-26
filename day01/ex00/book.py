import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        #initialize name
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.name = name
        #initialize last update
        if not isinstance(last_update, datetime.datetime):
            raise TypeError("Last update must be datetime")
        self.last_update = last_update
        #initialize creation date
        if not isinstance(creation_date, datetime.datetime):
            raise TypeError("Creation date must be a datetime")
        self.creation_date = creation_date
        #initialize recipes_list
        check_dict = {'starter': 1, 'lunch': 2, 'dessert': 3}
        if not isinstance(recipes_list, dict):
            raise TypeError("Recipes list must be dict")
        if not check_dict.keys() == recipes_list.keys():
            raise ValueError('Recipes_list must contain the keys "starter", "lunch" and "dessert"')
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if isinstance(name, Recipe):
            for elem in self.recipes_list.values():
                if elem and isinstance(elem, list):
                    for obj in elem:
                        if obj == name:
                            print(obj)
                elif elem and name == elem:
                    print(elem)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list.keys():
            return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if self.recipes_list[recipe.recipe_type] is None:
                self.recipes_list[recipe.recipe_type] = [recipe]
            else:
                self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print (recipe, 'is not an instance of Recipe')
