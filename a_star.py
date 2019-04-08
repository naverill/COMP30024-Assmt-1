from move import Move
from search import print_board

class AStar:
    def __init__(self, board_dict, start_hexs, goal_hexs, obstacles):
        self._init_state = board_dict
        self._start = start_hexs
        self._goal = goal_hexs
        self._obstacles = obstacles
        self._colour

    def a_star(self):
        start = Move(None, self._start)
        start.set_g(0)

        end = Move(None, self.goal)
        end.set_g(0)

        unexplored = []
        explored = []

        unexplored.append(start)

        while len(unexplored) > 0:
            curr_index = 0
            curr_move = unexplored.get(curr_index)

            for i, move in enumerate(unexplored):
                if move.f() < curr_move.f():
                    curr_move = move
                    curr_index = i

            unexplored.pop(curr_index)
            explored.append(curr_move)

            if curr_move.equal(end):
                path = []
                current = curr_move
                while current is not None:
                    path.append(current)
                    current = current.parent()

                return path[::-1]

        children = []
        for piece in curr_move.state().values():
            for coordinate in piece.get_neighbours():
                action = "MOVE"

                new_hex = self.board_dict[coordinate]

                if self._obstacles.contains(new_hex.get_type()):
                    new_hex = new_hex.jump(piece, self.board_dict)

                    if self._is_valid_jump(new_hex):
                        action = "JUMP"
                    else:
                        continue

                new_state = curr_move.state()
                new_state.remove(piece)
                new_state[coordinate] = new_hex

                new_move = Move(curr_move, new_state, action)

                children.append(new_move)

        for child in children:
            if explored.contains(child):
                continue

            child.set_g(curr_move.g() + child.cost)

            if unexplored.contains(child):
                i = unexplored.index(child)
                if child.g() > unexplored[i].g():
                    continue

            explored.append(child)

    def _is_valid_jump(self, hex):
        if self.obstacles.contains(hex.get_type()):
            return False
        elif self._goal.contains(hex.get_coordinate()):
            return False
        return True
