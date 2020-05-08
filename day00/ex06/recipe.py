recipe = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'time': 15
    }
}

while (1):
    select = input("""please type a number from 1 to 5:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n""")

    if select == '1':
        s = input("Please enter the recipe's name to add:\n")
        i = list(
            input(f"Please enter the list of ingredients of {s}:\n").split()
        )
        m = input(f"Please enter the type of meal of {s}:\n")
        t = input(f"Please enter the preparation time in minutes of {s}:\n")
        recipe[s] = {
            'ingredients': i,
            'meal': m,
            'time': t
        }

    elif select == '2':
        s = input("Please enter the recipe's name to delete:\n")
        del recipe[s]

    elif select == '3':
        s = input("Please enter the recipe's name to get its details:\n")
        if (s in recipe):
            print(f"Recipe for {s}:")
            print(f"Ingredients list: {recipe[s]['ingredients']}")
            print(f"To be eaten for {recipe[s]['meal']}")
            print(f"Takes {recipe[s]['time']} minutes of cooking\n")
        else:
            print("the recipe is not in cookbook\n")

    elif select == '4':
        for s in recipe:
            print(f"Recipe for {s}:")
            print(f"Ingredients list: {recipe[s]['ingredients']}")
            print(f"To be eaten for {recipe[s]['meal']}")
            print(f"Takes {recipe[s]['time']} minutes of cooking\n")

    elif select == '5':
        print("\nCookbook closed")
        exit()

    else:
        print("This option does not exist, please type a number from 1 to 5.")
        print("To exit, enter 5.\n")
