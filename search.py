"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part A: Searching

Authors:
"""

import sys
import json
from collections import defaultdict
from hex import Hex
import a_star
from datetime import datetime


def main():
    board_dict = defaultdict()

    ran = range(-Hex.BOARD_SIZE, +Hex.BOARD_SIZE+1)
    for q, r in [(q,r) for q in ran for r in ran if -q-r in ran]:
        board_dict[(q, r)] = Hex(q, r)

    start_hexs = {}
    obstacles = set()

    with open(sys.argv[1]) as file:
        data = json.load(file)
        blocks = [tuple(l) for l in data['blocks']]
        pieces = [tuple(l) for l in data['pieces']]
        colour = data["colour"]

        for block in blocks:
            board_dict[block].set_type("block")
            obstacles.add("block")

        for piece in pieces:
            q, r = piece
            start_hexs[piece] = Hex(q, r, colour)
            obstacles.add(colour)

    print_board(board_dict, debug=True)
    goal_hexs = find_goals(colour)
    print(start_hexs.keys())

    start = datetime.now()
    search = a_star.AStar(board_dict, start_hexs, goal_hexs, obstacles)
    end = datetime.now()
    path = search.a_star()
    print("Time Taken: {}".format(end - start))

    output_paths(path, board_dict)

    # TODO: Search for and output winning sequence of moves

    # ...

def output_paths(path, empty_board=None):
    if path is None:
        print("Empty path")
        return
    for move in path:
        move.print_move()

        if empty_board:
            board = {key: value.copy() for key, value in empty_board.items()}
            board.update(move.state())
            print_board(board)


def print_board(board_dict, message="", debug=False, **kwargs):
    """
    Helper function to print a drawing of a hexagonal board's contents.

    Arguments:

    * `board_dict` -- dictionary with tuples for keys and anything printable
    for values. The tuple keys are interpreted as hexagonal coordinates (using
    the axial coordinate system outlined in the project specification) and the
    values are formatted as strings and placed in the drawing at the corres-
    ponding location (only the first 5 characters of each string are used, to
    keep the drawings small). Coordinates with missing values are left blank.

    Keyword arguments:

    * `message` -- an optional message to include on the first line of the
    drawing (above the board) -- default `""` (resulting in a blank message).
    * `debug` -- for a larger board drawing that includes the coordinates
    inside each hex, set this to `True` -- default `False`.
    * Or, any other keyword arguments! They will be forwarded to `print()`.
    """

    # Set up the board template:
    if not debug:
        # Use the normal board template (smaller, not showing coordinates)
        template = """# {0}
#           .-'-._.-'-._.-'-._.-'-.
#          |{16:}|{23:}|{29:}|{34:}|
#        .-'-._.-'-._.-'-._.-'-._.-'-.
#       |{10:}|{17:}|{24:}|{30:}|{35:}|
#     .-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
#    |{05:}|{11:}|{18:}|{25:}|{31:}|{36:}|
#  .-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-.
# |{01:}|{06:}|{12:}|{19:}|{26:}|{32:}|{37:}|
# '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
#    |{02:}|{07:}|{13:}|{20:}|{27:}|{33:}|
#    '-._.-'-._.-'-._.-'-._.-'-._.-'-._.-'
#       |{03:}|{08:}|{14:}|{21:}|{28:}|
#       '-._.-'-._.-'-._.-'-._.-'-._.-'
#          |{04:}|{09:}|{15:}|{22:}|
#          '-._.-'-._.-'-._.-'-._.-'"""
    else:
        # Use the debug board template (larger, showing coordinates)
        template = """# {0}
#              ,-' `-._,-' `-._,-' `-._,-' `-.
#             | {16:} | {23:} | {29:} | {34:} |
#             |  0,-3 |  1,-3 |  2,-3 |  3,-3 |
#          ,-' `-._,-' `-._,-' `-._,-' `-._,-' `-.
#         | {10:} | {17:} | {24:} | {30:} | {35:} |
#         | -1,-2 |  0,-2 |  1,-2 |  2,-2 |  3,-2 |
#      ,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-.
#     | {05:} | {11:} | {18:} | {25:} | {31:} | {36:} |
#     | -2,-1 | -1,-1 |  0,-1 |  1,-1 |  2,-1 |  3,-1 |
#  ,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-.
# | {01:} | {06:} | {12:} | {19:} | {26:} | {32:} | {37:} |
# | -3, 0 | -2, 0 | -1, 0 |  0, 0 |  1, 0 |  2, 0 |  3, 0 |
#  `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-'
#     | {02:} | {07:} | {13:} | {20:} | {27:} | {33:} |
#     | -3, 1 | -2, 1 | -1, 1 |  0, 1 |  1, 1 |  2, 1 |
#      `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-'
#         | {03:} | {08:} | {14:} | {21:} | {28:} |
#         | -3, 2 | -2, 2 | -1, 2 |  0, 2 |  1, 2 | key:
#          `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' ,-' `-.
#             | {04:} | {09:} | {15:} | {22:} |   | input |
#             | -3, 3 | -2, 3 | -1, 3 |  0, 3 |   |  q, r |
#              `-._,-' `-._,-' `-._,-' `-._,-'     `-._,-'"""

    # prepare the provided board contents as strings, formatted to size.
    ran = range(-Hex.BOARD_SIZE, +Hex.BOARD_SIZE+1)
    cells = []
    for qr in [(q,r) for q in ran for r in ran if -q-r in ran]:
        if qr in board_dict:
            cell = str(board_dict[qr].get_type()).center(5)
        else:
            cell = "     " # 5 spaces will fill a cell
        cells.append(cell)

    # fill in the template to create the board drawing, then print!
    board = template.format(message, *cells)
    print(board, **kwargs)

def find_goals(colour):
    green = [(-3, 4), (-2, 4),  (-1, 4), (0, 4)]
    red = [(4, -3), (4, -2), (4, -1), (4, 0)]
    blue = [(-4, 0), (-1, -3), (-2, -2), (-3, -1)]

    if colour == "green":
        coordinates = green
    elif colour == "red":
        coordinates = red
    elif colour == "blue":
        coordinates = blue

    return {(q, r): Hex(q, r, "goal") for q, r in coordinates}

# when this module is executed, run the `main` function:
if __name__ == '__main__':
    main()
