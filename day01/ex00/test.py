from book import Book
from recipe import Recipe
import datetime

salad = Recipe(name='Salad', cooking_lvl=1, cooking_time=10, ingredients=['salad', 'Tomato', 'Ham'], description='A delicious salad.', recipe_type='lunch')
ScrambledEgg = Recipe(name='ScrambledEgg', cooking_lvl=2, cooking_time=20, ingredients=['egg', 'milk', 'butter', 'salt'], description='Food easy to make.', recipe_type='starter')
FriedPotato = Recipe(name='FriedPotato', cooking_lvl=2, cooking_time=40, ingredients=['potato', 'oil', 'salt'], description='Food eaten with burger.', recipe_type='lunch')
Shouldnotwork = 'Salad'

rcp_dict = dict.fromkeys(['starter', 'lunch', 'dessert'])
my_book = Book(name="Recipe book", last_update=datetime.datetime.now(), creation_date=datetime.datetime.now(), recipes_list=rcp_dict)
my_book.add_recipe(salad)
my_book.add_recipe(ScrambledEgg)
my_book.add_recipe(FriedPotato)
print('Three recipes added. Next one wont work.')
my_book.add_recipe(Shouldnotwork)  # should not work as it is not an instance of Recipe class

print('\n---- Recipe for ScrambledEgg ----')
my_book.get_recipe_by_name(ScrambledEgg)
print('---- Recipe for salad ----')
my_book.get_recipe_by_name(salad)
print('---- Recipe for FriedPotato ----')
my_book.get_recipe_by_name(FriedPotato)

print('---- Starter recipes ----')
starter_list = my_book.get_recipes_by_types('starter')
if starter_list is not None:
    if isinstance(starter_list, list):
        for elem in starter_list:
            print(str(elem))
    else:
        print(str(starter_list))
else:
    print("None")

print('---- Lunch recipes ----')
lunch_list = my_book.get_recipes_by_types('lunch')
if lunch_list is not None:
    if isinstance(lunch_list, list):
        for elem in lunch_list:
            print(str(elem))
    else:
        print(str(lunch_list))
else:
    print("None")

print('---- Dessert recipes ----')
dessert_list = my_book.get_recipes_by_types('dessert')
if dessert_list is not None:
    if isinstance(dessert_list, list):
        for elem in dessert_list:
            print(str(elem))
    else:
        print(str(dessert_list))
else:
    print("None")
