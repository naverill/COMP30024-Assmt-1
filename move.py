
class Move:
    def __init__(self, parent, state, action='', cost=1):
        self._parent = parent   # Move
        self._state = state # Hex
        self.action = action
        self._g = None
        self._h = self._init_h()
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

    def _init_h(self, h):
        # shortest distance to goal node
        path_cost = []
        for piece in self._state.values():
            goal_dist = []
            for goal in self._goal.values():
                goal_dist.append(self._hex_distance(piece, goal))
            path_cost.append(min(goal_dist))
        return sum(path_cost)

    def get_moved_piece(self):
        new_pos_set = set(self._state.key())
        old_pos_set = set(self._parent.state().key())
        old_pos = old_pos_set.difference(new_pos_set)
        new_pos = new_pos_set.difference(old_pos_set)
        return old_pos, new_pos

    def print_move(self):
        old_pos, new_pos = self.get_moved_piece()
        action = self.action()
        print("{} from {} to {}.".format(action, old_pos, new_pos))

    def action(self):
        if not self._state.get_type() == "EXIT":
            return "EXIT"
        else:
            return self._action
        pass

    def __eq__(self, other):
        return self._state.equal(self.other.state())

    @staticmethod
    def _hex_distance(a, b):
        return (abs(a.q - b.q) + abs(a.q + a.r - b.q - b.r) + abs(a.r - b.r)) / 2

