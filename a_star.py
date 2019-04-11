from move import Move

class AStar:
    def __init__(self, board_dict, start_hexs, goal_hexs, obstacles):
        self._empty_board = board_dict
        self._start = start_hexs
        self._goals = goal_hexs
        self._obstacles = obstacles

    def a_star(self):
        start = Move(None, self._start)
        start.set_g(0)
        start.set_h(self._goals)

        end = Move(None, self._goals)
        end.set_g(0)
        end.set_h(self._goals)

        unexplored = []
        explored = []

        unexplored.append(start)

        while len(unexplored) > 0:
            curr_index = 0
            curr_move = unexplored[curr_index]

            for i, move in enumerate(unexplored):
                if move.f() < curr_move.f():
                    curr_move = move
                    curr_index = i

            unexplored.pop(curr_index)
            explored.append(curr_move)

            if curr_move == end:
                path = []
                current = curr_move
                while current is not None:
                    path.append(current)
                    current = current.parent()
               # print(path)
                return path[::-1]

        children = []
        board_state = self.update_board(curr_move.state().values())
        for piece in curr_move.state().values():
            for coordinate in piece.get_neighbours():
                action = "MOVE"

                new_hex = board_state[coordinate]

                if new_hex.get_type() in self._obstacles:
                    new_hex = new_hex.jump(piece, board_state)

                    if self._is_valid_jump(new_hex):
                        action = "JUMP"
                    else:
                        continue

                new_state = dict(curr_move.state())

               # point = piece.get_coordinate()
                #TODO: Get the key for the piece value and pop that
                for key, value in curr_move.state().items():
                    if value == piece:
                       p_key = key

                del new_state[p_key]
                #new_state.pop(piece_key)
                new_state[coordinate] = new_hex

                new_move = Move(curr_move, new_state, action)

                children.append(new_move)

        for child in children:
            if child in explored:
                continue

            child.set_g(curr_move.g() + child.cost)
            child.set_h(self._goals)

            if child in unexplored:
                i = unexplored.index(child)
                if child.g() > unexplored[i].g():
                    continue

            explored.append(child)

    def update_board(self, state):
        board = self._empty_board.copy()

        for hex in state:
            #print(hex)
            coordinate = hex.get_coordinate()
            board[coordinate] = hex

        return board

    def _is_valid_jump(self, hex):
        if hex.get_type() in self._obstacles:
            return False
        elif hex.get_coordinate() in self._goals:
            return False
        return True
