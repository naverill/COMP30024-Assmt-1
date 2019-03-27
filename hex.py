
class Hex:
    BOARD_SIZE = 3

    def __init__(self, q=-1, r=-1, type=None):
        self._q = q
        self._r = r
        self._type = type

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_coordinate(self):
        return self._q, self._r
    
    def get_q(self):
        return self._q

    def get_r(self):
        return self._r

    def left(self):
        if not Hex.is_valid(self.q - 1, self.r):
            return None
        return Hex(self._q - 1, self._r)

    def right(self):
        if not Hex.is_valid(self.q + 1, self.r):
            return None
        return Hex(self._q + 1, self._r)

    def top_left(self):
        if not Hex.is_valid(self.q, self.r - 1):
            return None
        return Hex(self._q, self._r - 1)

    def top_right(self):
        if not Hex.is_valid(self.q + 1, self.r - 1):
            return None
        return Hex(self._q + 1, self._r - 1)

    def bottom_left(self):
        if not Hex.is_valid(self.q - 1, self.r + 1):
            return None
        return Hex(self._q - 1, self._r + 1)

    def bottom_right(self):
        if not Hex.is_valid(self.q, self.r + 1):
            return None
        return Hex(self._q, self._r + 1)

    @staticmethod
    def is_valid(q, r):
        return q >= 0 and q <= Hex.BOARD_SIZE and r >= 0 and r <= Hex.BOARD_SIZE
