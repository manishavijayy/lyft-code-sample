"""
File:    silicon_crisis.py
Author:  Manisha Vijay
Date:    5/14/21
Section: 11
E-mail:  mvijay1@umbc.edu
Description:
    silicon crisis file

"""
QUIT_STRING = "quit"
import json

def read_recipe_maker(file):
    """
    read recipe maker file using json
    :param file: user input file name
    :return: recipe maker dictionary
    """
    read_file = open(file, 'r')
    string = read_file.read()
    recipes = json.loads(string)
    return recipes

def end_turn(mines, factories, stockpile, currently_making):
    """
    ends turn and adds to the stockpile
    :param mines: list of set mines
    :param factories: list of set factories
    :param stockpile: finished stockpile dictionary
    :param currently_making: currently set tasks
    :return: stockpile
    """
    for key in currently_making:
        if key != key + 1:
            stockpile[key] = ''

        if key == key + 1:
            total = currently_making[key] + currently_making[key + 1]
            stockpile[key] = total
        else:
            stockpile[key] = currently_making[key]


    return stockpile


def select_next_action(mines, factories, materials, quantities, data, stockpile, next_action):
    """
    select next action commands, set and display commands
    :param mines: empty list to store set mines
    :param factories: empty list to store set factories
    :param materials: empty list to store raw materials
    :param quantities: empty list to store quantities of factories, mines, etc
    :param data: recipe maker dictionary
    :param stockpile: stockpile dictionary
    :param next_action: user input select next action
    :return: loop for select next action
    """

    action_list = next_action.split()
    turn = 0
    currently_making = {}
    if action_list[0] == "set" and action_list[1] == "mine":
        mine_count = 0
        quantities['mines'] = ''
        mine = {}
        mine["output"] = "mine"
        mine["makes"] = ""
        mine["output_counts"] = data["recipes"]["mine"]["output_count"]
        mine["parts"] = data["recipes"]["mine"]["parts"]
        mines.append(mine)
        mines[int(action_list[2])]["makes"] = action_list[3]
        currently_making[mines['makes']] = mines['parts'][mines["makes"]]

        mine_count += 1
        quantities['mines'] = mine_count
    elif action_list[0] == "set" and action_list[1] == "factory":
        factory_count = 0
        quantities['factories'] = ''
        for i in range(2):
            factory = {}
            factory['output'] = 'factory'
            factory['makes'] = ''
            factory['output_counts'] = data['recipes']['factory']['output_count']
            factory['parts'] = data['recipes']['factory']['parts']
            factories.append(factory)
            factory_count += 1
        factories[int(action_list[2])]['makes'] = action_list[3]
        currently_making[factories['makes']] = factories['parts'][factories['makes']]
        quantities['factories'] = factory_count



    elif action_list[0] == "display" and action_list[1] == "mines":

        for m in range(len(mines)):
            print("\tMine", m)
            if mines[m]['makes']:
                make = mines[m]['makes']
                print('\t\t', make, "mine producing", mines[m]['parts'][make], "per turn")
            else:
                print("Mine Currently Inactive")


    elif action_list[0] == "display" and action_list[1] == "factories":
        for f in range(len(factories)):
            print("\tFactory", f)
            if factories[f]['makes']:
                make = factories[f]['makes']
                print('\t\t', make, "factory producing", factories[f]['parts'][make], "per turn")
            else:
                print("\t\tFactory Currently Inactive")
    elif action_list[0] == "display" and action_list[1] == "stockpile":
        print(":::Current Stockpile:::")
        print("\t", stockpile)
    elif action_list[0] == "display" and action_list[1] == "raw":
        print(":::raw materials:::")
        for raw in data['raw materials']:
            materials.append(raw)
            print("\t", raw, ":", data['raw materials'][raw])
    elif action_list[0] == "display" and action_list[1] == "recipes":
        print(":::Recipes:::")
        for recipe in data['recipes']:
            print("\t", recipe, "produced in increments of", data['recipes'][recipe]['output_count'])
            print("\tRequire materials: ")
            for part in data['recipes'][recipe]['parts']:
                print("\t\t", part, ":", data['recipes'][recipe]['parts'][part])

    elif action_list[0] == "end" and action_list[1] == "turn":
        turn += 1
        stockpile = end_turn(mines, factories, stockpile, currently_making)
        print("Mining...")
        print("Making...")
        print("Turn", turn, "Complete")


    next_action = input("Select Next Action>> ")
    return next_action
def run_game(data):
    """
    runs the whole game, including select next action loop
    :param data: read recipe maker dictionary
    :return: game plays
    """

    mines_list = [] # mines
    factories_list = []
    materials_list = []
    stock_pile = {}
    quantities = {} # key called mines with overall number of mines, key called factories with amount of factories, etc
    next_action = input("Select Next Action>> ")
    action = select_next_action(mines_list, factories_list, materials_list, quantities, data, stock_pile, next_action)
    while action != QUIT_STRING:
        action = select_next_action(mines_list, factories_list, materials_list, quantities, data, stock_pile, action)

if __name__ == "__main__":
    recipe_file = input("Enter SC Recipe File Name: ")
    data = read_recipe_maker(recipe_file)
    run_game(data)
