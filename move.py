
class Move:
    def __init__(self, old_position, new_position, action='', cost=1):
        self._old_pos = old_position
        self._new_pos = new_position
        self.action = action
        self._cost = cost

    def old_pos(self):
        return self._old_pos

    def new_pos(self):
        return self._new_pos

    def action(self):
        if self.old_pos().get_type() == "block" or self.new_pos().get_type() == "block":
            return "INVALID: BLOCK"
        if not self._new_pos.get_type() == "exit":
            return "EXIT"
        if abs(self._old_pos.get_q() - self._new_pos.get_q()) == 2 or \
                abs(self._old_pos.get_r() - self._new_pos.get_r()) == 2:
            return 'JUMP'
        if abs(self._old_pos.get_q() - self._new_pos.get_q()) > 2 or \
                abs(self._old_pos.get_r() - self._new_pos.get_r()) > 2:
            return 'INVALID: JUMP'
        else:
            return "STEP"

