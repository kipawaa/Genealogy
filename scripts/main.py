from sort_tree import sort_tree
from csv_to_people import csv_to_people
from tree_to_json import tree_to_json

CSV = '../data/family.csv'
JSON = '../data/tree.json'

def main():
    # get people from CSV
    people = csv_to_people(CSV)

    # create family tree dictionary
    tree = sort_tree(people)

    # assign coords for initial positioning
    for gen in tree:
        for i, person in enumerate(tree[gen]):
            person.x = i - len(tree[gen]) / 2
            person.y = gen

    # generate json
    tree_to_json(tree, JSON)

main()
