import copy

class Move:
    def __init__(self, parent, state, goals, action='', cost=0.5):
        self._parent = parent   # Move
        self._state = state # Hex
        self._goals = goals
        self.action = action
        self._g = None
        self._h = None
        self.cost = cost

    def state(self):
        return self._state

    def parent(self):
        return self._parent

    def g(self):
        return self._g

    def h(self):
        return self._h

    def f(self):
        return self._g + self._h

    def set_g(self, g):
        self._g = g

    def set_h(self):
        # shortest distance to goal node
        path_cost = []
        for piece in self._state.values():
            goal_dist = []
            for goal in self._goals.values():
                goal_dist.append(self._hex_distance(piece, goal))
            path_cost.append(min(goal_dist))

        self._h = sum(path_cost)

    def get_transition(self):
        if not self._parent:
            return None, None
        new_pos_set = set(self._state.keys())
        old_pos_set = set(self._parent.state().keys())
        old_pos = old_pos_set.difference(new_pos_set)
        new_pos = new_pos_set.difference(old_pos_set)
        return old_pos, new_pos

    def print_move(self):
        old_pos, new_pos = self.get_transition()
        if not old_pos or not new_pos:
            return
        action = self.action
        print("{} from {} to {}.".format(action, old_pos, new_pos))

    def action(self):
        # if not self._state.get_type() == "EXIT":
        #     return "EXIT"
        # else:
        return self._action

    def end(self):
        return all([coordinate in self._goals.keys() for coordinate in self._state.keys()])

    def get_children(self, board, obstacles):
        children = []
        # print(self._state.keys())
        for piece in self._state.values():
            if piece.get_coordinate() in self._goals:
                continue
            # print(piece.get_coordinate())
            for coordinate in self._get_neighbours(piece):
                action = "MOVE"

                new_hex = self._get_hex(coordinate, board)

                if new_hex.get_type() in obstacles:
                    new_hex = new_hex.jump(piece, board)

                    if self._is_valid_jump(new_hex, obstacles):
                        action = "JUMP"
                    else:
                        continue
                new_hex.set_type("red") #todo(naverill) change from hard-coding

                if new_hex.get_coordinate() in self._goals.keys():
                    action = "EXIT"

                new_state = {key: value for key, value in self._state.items()}
                # print(new_state.keys())
                new_state.pop(piece.get_coordinate())

                new_state[new_hex.get_coordinate()] = new_hex

                new_move = Move(self, new_state, self._goals, action)

                children.append(new_move)

        return children

    def _get_neighbours(self, piece):
        neighbours = piece.get_neighbours()

        for coordinate, goal in self._goals.items():
            if self._is_adjacent(piece, goal):
                neighbours.append(coordinate)

        return neighbours

    def _get_hex(self, coordinate, board):
        return board[coordinate].copy() if board.get(coordinate) else self._goals.get(coordinate).copy()

    def _is_valid_jump(self, hex, obstacles):
        if hex is None:
            return False
        if hex.get_type() in obstacles:
            return False
        elif hex.get_coordinate() in self._goals:
            return False
        return True

    def _is_adjacent(self, piece, other):
        return self._hex_distance(piece, other) == 1

    @staticmethod
    def _hex_distance(a, b):
        return float((abs(a.q() - b.q()) + abs(a.q() + a.r() - b.q() - b.r()) + abs(a.r() - b.r()))) / 2.0

    def __eq__(self, other):
        # return sorted(self._state.keys()) == sorted(other.state().keys())
        return sorted(self.state().values()) == sorted(other.state().values())

    def __lt__(self, other):
        return sorted(self.state().values()) < sorted(other.state().values())

    def __gt__(self, other):
        return sorted(self.state().values()) > sorted(other.state().values())

