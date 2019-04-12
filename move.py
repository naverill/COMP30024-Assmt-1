import copy
import math


class Move:
    def __init__(self, parent, state, goals, action='', cost=0.5):
        self._parent = parent   # previous Move
        self._state = state  # Hex
        self._goals = goals  # tiles just outside area of exit for required colour
        self.action = action
        self._g = None
        self._h = None
        self.cost = cost

    def get_children(self, board, obstacles):  # returns a list of valid children for A* to explore
        children = []

        for piece in self._state.values():  # loop through all pieces in current state
            if piece.get_coordinate() in self._goals:  # don't return neighbours if piece is already at goal
                continue

            for coordinate in self._get_neighbours(piece):
                new_hex = self._get_hex(coordinate, board)  # get hex tile for neighbouring coordinate

                # return action abd hex tile for that movement
                new_hex, action = self._action(piece, new_hex, obstacles, board)

                if action == "INVALID":  # check if action is valid
                    continue
                # check if neighbour is a goal
                new_hex.set_type("goal" if self._is_goal(new_hex) else piece.get_type())

                new_state = self._update_state(piece, new_hex)

                new_move = Move(self, new_state, self._goals, action)

                children.append(new_move)

        return children

    def _get_neighbours(self, piece):  # adds any goal tiles which may be neighbours to the neighbours list
        neighbours = piece.get_neighbours()

        for coordinate, goal in self._goals.items():
            if self._is_adjacent(piece, goal):
                neighbours.append(coordinate)

        return neighbours

    def _update_state(self, piece, new_hex):
        state = {key: value for key, value in self._state.items()}

        state.pop(piece.get_coordinate())  # remove old position of moved piece from current state

        state[new_hex.get_coordinate()] = new_hex  # add new, moved piece to new state

        return state

    def get_transition(self):  # returns movement of piece in final path, old coordinates and new coordinates
        if not self._parent:  # check if parent exists
            return None, None
        new_pos_set = set(self._state.keys())
        old_pos_set = set(self._parent.state().keys())
        old_pos = old_pos_set.difference(new_pos_set)
        new_pos = new_pos_set.difference(old_pos_set)
        return old_pos, new_pos

    def print_move(self):  # prints move in correct format
        old_pos, new_pos = self.get_transition()
        if not old_pos:
            return
        action = self.action
        if action == "EXIT":
            print("{} from {}.".format(action, list(old_pos)[0]))
        else:
            print("{} from {} to {}.".format(action, list(old_pos)[0], list(new_pos)[0]))

    def _action(self, curr_hex, new_hex, obstacles, board):  # determine what type of move piece is doing

        if self._is_goal(new_hex):  # if move is to a goal tile, action is exit
            return new_hex, "EXIT"

        elif self._is_obstacle(new_hex, obstacles):  # check if neighbour is a block or another piece
            new_hex = curr_hex.jump(new_hex, board)

            if self._is_valid_jump(new_hex, obstacles):  # check if tile can jump
                return new_hex, "JUMP"
            else:
                return new_hex, "INVALID"
        else:
            return new_hex, "MOVE"  # otherwise its just a normal move

    def _is_valid_jump(self, hex, obstacles):
        if hex is None:
            return False
        if hex.get_type() in obstacles:  # check if jump is to another obstacle
            return False
        elif hex.get_coordinate() in self._goals:  # check if jump is to a goal tile
            return False
        return True

    def set_g(self, g):
        self._g = g

    def set_h(self):  # returns h cost of a tile
        # shortest distance to goal node
        path_cost = []
        for piece in self._state.values():  # loop through each piece in current state
            goal_dist = []
            for goal in self._goals.values():
                opt_dist = self._min_dist(self._hex_distance(piece, goal))  # get closest goal node and add to list
                #opt_dist = self._hex_distance(piece, goal)
                goal_dist.append(opt_dist)
            path_cost.append(min(goal_dist))
            #print("Goal dist", goal_dist)
        #print("path cost", path_cost)

        self._h = sum(path_cost)  # returns h cost of all pieces, to each piece's nearest goal, combined

    def _is_adjacent(self, piece, other):
        return self._hex_distance(piece, other) == 1

    @staticmethod
    # function inspired from: https://www.redblobgames.com/grids/hexagons/
    def _hex_distance(a, b):  # calculates distance between 2 hex tiles based on axial coordinates
        return float((abs(a.q() - b.q()) + abs(a.q() + a.r() - b.q() - b.r()) + abs(a.r() - b.r()))) / 2.0

    def state(self):
        return self._state

    def _min_dist(self, dist):  # heuristic function helper, length of path assuming blocks on alternate hexes
        if dist % 2 == 0:
            return int(dist / 2 + 1)
        else:
            return math.ceil(dist / 2.0)

    def parent(self):
        return self._parent

    def g(self):
        return self._g

    def h(self):
        return self._h

    def f(self):
        return self._g + self._h

    def action(self):
        return self._action

    def end(self):  # checks if all pieces have reached goal
        return all([coordinate in self._goals.keys() for coordinate in self._state.keys()])

    def _get_hex(self, coordinate, board):  # returns the hex on a board given the coordinate
        return board[coordinate].copy() if board.get(coordinate) else self._goals.get(coordinate).copy()

    def _is_goal(self, piece):
        return piece.get_coordinate() in self._goals.keys()  # check if a piece has reached the goal

    def _is_obstacle(self, piece, obstacles):  # returns if an object is preventing a move
        return piece.get_type() in obstacles

    def __eq__(self, other):
        # return sorted(self._state.keys()) == sorted(other.state().keys())
        return sorted(self.state().values()) == sorted(other.state().values())  # check if 2 tiles are the same

    def __lt__(self, other):
        return sorted(self.state().values()) < sorted(other.state().values())

    def __gt__(self, other):
        return sorted(self.state().values()) > sorted(other.state().values())

