
class Move:
    def __init__(self, old_position, new_position, cost=1):
        self._old_pos = old_position
        self._new_pos = new_position
        self._cost = cost

    def get_old_pos(self):
        return self._old_pos

    def get_new_pos(self):
        return self._new_pos