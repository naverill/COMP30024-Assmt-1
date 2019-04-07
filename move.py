
class Move:
    def __init__(self, parent, position, action='', cost=1):
        self._parent = parent   # Move
        self._position = position # Hex
        self.action = action
        self._g = None
        self._h = None
        self.cost = cost

    def position(self):
        return self._position

    def parent(self):
        return self._parent

    def g(self):
        return self._g

    def h(self):
        return self._h

    def f(self):
        return self._g + self._h

    def equal(self, other):
        return self._position.equal(other)

    

    # def action(self):
    #     if self.parent().position().get_type() == "block" or self.position().get_type() == "block":
    #         return "INVALID: BLOCK"
    #     if not self._position.get_type() == "exit":
    #         return "EXIT"
    #     if abs(self._parent.get_q() - self._position.get_q()) == 2 or \
    #             abs(self._parent.get_r() - self._position.get_r()) == 2:
    #         return 'JUMP'
    #     if abs(self._parent.get_q() - self._position.get_q()) > 2 or \
    #             abs(self._parent.get_r() - self._position.get_r()) > 2:
    #         return 'INVALID: JUMP'
    #     else:
    #         return "STEP"
