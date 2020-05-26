class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        #initialize name
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.name = name
        #initialize cooking level
        if not isinstance(cooking_lvl, int):
            raise TypeError("Cooking lvl must be int")
        if not cooking_lvl in range (1, 6):
            raise ValueError("Range of cooking_lvl is 1 to 5")
        self.cooking_lvl = cooking_lvl
        #initialize cooking time
        if not isinstance(cooking_time, int):
            raise TypeError("Cooking time must be int")
        if cooking_time < 0:
            raise ValueError("Cooking time must be positive number")
        self.cooking_time = cooking_time
        #initialize ingredients
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients must be list")
        for elem in ingredients:
            if not isinstance(elem, str):
                raise TypeError("All elements of ingredients must be str")
        self.ingredients = ingredients
        #initialize description
        if description is not None:
            if not isinstance(description, str):
                raise TypeError("Description must be str")
            self.description = description
        #initialize recipe type
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type must be str")
        if not recipe_type in ["starter", "lunch", "dessert"]:
            raise ValueError("Please type the recipe among starter, lunch and dessert")
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f'This is the recipe for {self.name}.\n\
Cooking level: {self.cooking_lvl}\n\
Cooking time: {self.cooking_time}\n\
Ingredients: {self.ingredients}\n\
This recipe is for {self.recipe_type}.\n\
{self.description}\n'
        return txt
