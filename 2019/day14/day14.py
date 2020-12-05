from collections import defaultdict

def get_production_rules(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_quantity_and_ingredient(output):
    info = output.split(' ')
    return (int(info[0]), info[1])

def get_ingredients(ingredients):
    ingredients_list = ingredients.replace(', ', '&').split('&')
    return tuple(map(get_quantity_and_ingredient, ingredients_list))

def get_ingredients_and_output(production_rule):
    rule = production_rule.split('=')
    ingredients, output = rule[0][:-1], rule[1][2:]
    ingredients = get_ingredients(ingredients)
    output = get_quantity_and_ingredient(output)
    return ingredients, output

def create_rule_map(production_rules):
    rule_map = defaultdict(list)
    for production_rule in production_rules:
        ingredients, output = get_ingredients_and_output(production_rule)
        rule_map[output[1]].append(output[0] + ingredients)
    return rule_map

def part1(rule_map, needed={1, "FUEL"}):
    if not needed:
        return 0
    return 1

def main():
    production_rules = get_production_rules("day14.in")
    rule_map = create_rule_map(production_rules)
    result = part1(rule_map)
    #part1
    print(result)


if __name__ == "__main__":
    main()