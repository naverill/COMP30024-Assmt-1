
class AStar:
    def __init__(self, board_dict, start_hexs, goals_hexs:
        self._init_state = board_dict
        self._start = start_hexs
        self._goal = goal_hexs


    def a_star(self):
        start = Move(None)
        start.set_g(0)
        start.set_h(0)

        end = Move(None, goal_hexs)
        end.set_g(0)
        end.set_h(0)

        open = []
        closed = []

        open.append(start)

        while len(open) > 0:
            curr_index = 0
            curr_move = open.get(curr_index)

            for i, move in enumerate(open):
                if item.f() < curr.f():
                    curr_move = move
                    curr_index = i

            open.pop(curr_index)
            closed.append(curr_move)

            if curr_move.equal(end_node):
                path = []
                current = curr_move
                while current is not None:
                    path.append(current.position())
                    current = current.parent()

                return path[::-1]

        children = {}
        for piece in curr_move.position().keys():
            for new in piece.get_neighbours():
                new_pos = curr_move.position()
                new_pos.remove(piece)
                new_pos[tuple(new.get_coordinate())] =  new

                new_move = Move(curr_move, new_pos)

                children.append(new_move)



        pass


    def _g(self, move):
        # path
        #
        return

    def _h(self):
        # shortest distance to goal node - #pieces/blocks in the way
        return self._hex_distance()

    def _hex_distance(self, a, b):
        return (abs(a.q - b.q) + abs(a.q + a.r - b.q - b.r) + abs(a.r - b.r)) / 2
