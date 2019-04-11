from move import Move
from priority_queue import PriorityQueue

class AStar:
    def __init__(self, board_dict, start_hexs, goal_hexs, obstacles):
        self._empty_board = board_dict
        self._start = start_hexs
        self._goals = goal_hexs
        self._obstacles = obstacles

    def a_star(self):
        start = Move(None, self._start, self._goals)
        start.set_g(0)
        start.set_h()

        frontier = PriorityQueue()
        explored = []

        frontier.put(start, start.f())

        while not frontier.empty():
            # frontier.print_costs()
            # print([move.get_transition() for move in frontier])
            curr_move = frontier.get()
            # print(curr_move.get_transition())
            explored.append(curr_move)

            if curr_move.end():
                break

            board_state = self.update_board(curr_move.state().values())
            children = curr_move.get_children(board_state, self._obstacles)

            for child in children:
                if child in explored:
                    continue

                child.set_g(curr_move.g() + child.cost)
                child.set_h()

                if child in frontier:
                    if child.g() > frontier.get(child).g():
                        continue

                frontier.put(child, child.f())

        path = []
        current = curr_move
        # print(curr_move)
        while current is not None:
            path.append(current)
            current = current.parent()
        # print(path)
        return path[::-1]

    def update_board(self, state):
        board = self._empty_board.copy()

        for hex in state:
            #print(hex)
            coordinate = hex.get_coordinate()
            board[coordinate] = hex

        return board
