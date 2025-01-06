"""
-------------------------------------------------------
[Food Class Utility Functions]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    name = input("Name: ")

    print("Origin")
    p = Food("Hokey Pokey Ice Cream", 10, True, 106)
    print(p.origins())
    origin = int(input(":"))

    vegetarian = input("Vegetarian (Y/N)")
    if vegetarian == "Y":
        vegetarian = True
    if vegetarian == "N":
        vegetarian = False

    calories = int(input("Calories:"))

    food = Food(name, origin, vegetarian == True, calories)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    line.strip()
    x = line.split("|")

    if x[2] == "True":
        x[2] = True
    if x[2] == "False":
        x[2] = False

    origin = int(x[1])

    calories = int(x[3])

    food = Food(x[0], origin, x[2], calories)

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    foods = []
    x = file_variable.readline()

    while x != "":
        i = read_food(x)

        foods.append(i)

        x = file_variable.readline()

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    for x in foods:
        line = (f"{x.name}|{x.origin}|{x.is_vegetarian}|{x.calories}\n")
        file_variable.write(line)
    return None


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    veggies = []

    for x in foods:
        if x.is_vegetarian == True:
            veggies.append(x)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    origins = []

    for i in range(len(foods)):
        fs = foods[i].origin
        if fs == origin:
            origins.append(foods[i])

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    # Your code here
    total = 0
    count = 0
    avg1 = 0

    for i in range(len(foods)):
        avg1 = foods[i].calories
        total += avg1
        count += 1

    avg = total // count

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    total_calories = 0
    count = 0

    for food in foods:
        if food.origin == origin:
            total_calories += food.calories
            count += 1

    if count > 0:
        avg = total_calories / count
    else:
        avg = 0

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    # Your code here
    foods.sort()
    print("Food                                Origin       Vegetarian Calories")
    print("----------------------------------- ------------ ---------- --------")
    for f in foods:
        print("{:<36s}{:<13s}{:<11s}{}".format(
            f.name, Food.ORIGIN[f.origin], str(f.is_vegetarian), str(f.calories)))

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []
    any_origin = False
    if origin == -1:
        any_origin = True
    any_cals = False
    if max_cals == 0:
        any_cals = True
    any_veg = False
    if is_veg == False:
        any_veg = True

    for f in foods:
        if not any_origin and f.origin != origin:
            continue
        if not any_cals and f.calories > max_cals:
            continue
        if is_veg != f.is_vegetarian:
            continue
        result.append(f)
    return result
