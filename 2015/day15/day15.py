def is_five_hundred_calories(recipe_map, recipe_amounts):
    calories = sum([recipe_amounts[recipe]*recipe_map[recipe][4] for recipe in recipe_map.keys()])
    return calories == 500

def get_score(recipe_map, recipe_amounts, five_hundred_calories):
    score = 1
    for i in range(4):
        score *= max(0, sum([recipe_amounts[recipe]*recipe_map[recipe][i] for recipe in recipe_map.keys()]))

    if not five_hundred_calories or is_five_hundred_calories(recipe_map, recipe_amounts):
        return score
    return 0

def get_best_recipe(recipe_map, recipes_remaining, recipe_amounts, five_hundred_calories = False, teaspoons_left = 100):
    if len(recipes_remaining) == 1:
        recipe_amounts[recipes_remaining[0]] = teaspoons_left
        return get_score(recipe_map, recipe_amounts, five_hundred_calories)
    
    max_score = None

    for i in range(teaspoons_left + 1):
        recipe_amounts[recipes_remaining[0]] = i
        if max_score is None:
            max_score = get_best_recipe(recipe_map, recipes_remaining[1:], recipe_amounts, five_hundred_calories, teaspoons_left - i)
        else:
            max_score = max(max_score, get_best_recipe(recipe_map, recipes_remaining[1:], recipe_amounts, five_hundred_calories, teaspoons_left - i))
    
    return max_score


def get_recipe_map(recipes):
    recipe_map = {}

    for recipe in recipes:
        recipe_info = recipe.replace(',', '').split(' ')
        recipe_map[recipe_info[0][:-1]] = (int(recipe_info[2]), int(recipe_info[4]), int(recipe_info[6]), int(recipe_info[8]), int(recipe_info[10]))

    return recipe_map

def get_recipes(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    recipes = get_recipes("day15input.txt")
    #(capacity, durability, flavor, texture, calories)
    #also, I disagree with the spelling of flavour for this problem
    recipe_map = get_recipe_map(recipes)
    recipe_amounts = {}
    result = get_best_recipe(recipe_map, list(recipe_map.keys()), recipe_amounts)
    #part 1
    print(result)

    result = get_best_recipe(recipe_map, list(recipe_map.keys()), recipe_amounts, True)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
