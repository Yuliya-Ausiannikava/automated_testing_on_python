"""
A program that reads data from a file and displays information about the club with the most wins.
"""

from pprint import pprint
import json

data_football_clubs = {
    "1": {
        "name": "Real Madrid",
        "country": "Spain",
        "victories": 15
    },
    "2": {
        "name": "AC Milan",
        "country": "Italy",
        "victories": 7
    },
    "3": {
        "name": "FC Bayern",
        "country": "Germany",
        "victories": 6
    }
}

with open("dataFC.json", "w", encoding='utf-8') as file_fc:
    json.dump(data_football_clubs, file_fc)


# Finds the team with the most wins
def parse_json(data):
    max_win = 0
    best_club = None
    for key in data:
        win = data[key]["victories"]
        max_win = max(max_win, win)
        if win == max_win:
            best_club = data[key]
    pprint(best_club, width=50)
    return best_club


# Reads the file and calls the "parse_json" function
def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data_fc = json.load(file)
        return parse_json(data_fc)


read_json('dataFC.json')
