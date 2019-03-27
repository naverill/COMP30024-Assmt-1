
class Hex:
    BOARD_SIZE = 3

    def __init__(self, q=-1, r=-1, type=''):
        self._q = q
        self._r = r
        self._type = type
        self.neighbours = [self.left, self.right, self.top_left, self.top_right, self.bottom_left, self.bottom_right]

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
        if not Hex.is_valid(self._q - 1, self._r):
            return None
        return self._q - 1, self._r

    def right(self):
        if not Hex.is_valid(self._q + 1, self._r):
            return None
        return self._q + 1, self._r

    def top_left(self):
        if not Hex.is_valid(self._q, self._r - 1):
            return None
        return self._q, self._r - 1

    def top_right(self):
        if not Hex.is_valid(self._q + 1, self._r - 1):
            return None
        return self._q + 1, self._r - 1

    def bottom_left(self):
        if not Hex.is_valid(self._q - 1, self._r + 1):
            return None
        return self._q - 1, self._r + 1

    def bottom_right(self):
        if not Hex.is_valid(self._q, self._r + 1):
            return None
        return self._q, self._r + 1

    def get_neighbours(self):
        neighbours = []
        for neighbour in self.neighbours:
            if neighbour():
                neighbours.append(neighbour())
        return neighbours

    @staticmethod
    def is_valid(q, r):
        ran = range(-Hex.BOARD_SIZE, Hex.BOARD_SIZE + 1)
        return -q-r in ran \
               and -Hex.BOARD_SIZE <= q <= Hex.BOARD_SIZE \
               and - Hex.BOARD_SIZE <= r <= Hex.BOARD_SIZE

