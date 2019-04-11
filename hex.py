
class Hex:
    BOARD_SIZE = 3

    def __init__(self, q=-1, r=-1, type=''):
        self._q = q
        self._r = r
        self._type = type
        self._neighbours = [self.left, self.right, self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_coordinate(self):
        return self._q, self._r

    def get_coordinate_string(self):
        return "(", + str(self.q) + ', ' + str(self.r) + ")"

    def q(self):
        return self._q

    def r(self):
        return self._r

    def set_q(self, value):
        self._q = value

    def set_r(self, value):
        self._r = value

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
        for neighbour in self._neighbours:
            if neighbour():
                neighbours.append(neighbour())
        return neighbours

    def jump(self, neighbour, board):
        opposite = self._opposite_neighbour(neighbour)

        if self.is_valid(opposite[0], opposite[1]):
            return board[opposite]
        else:
            return None

    def _opposite_neighbour(self, neighbour):
        #todo(naverill) test
        dist_q = neighbour.q() - self.q()
        dist_r = neighbour.r() - self.r()
        #dist = self.get_coordinate() - neighbour.get_coordinate()
        return neighbour.q() + dist_q, neighbour.r() + dist_r


    @staticmethod
    def is_valid(q, r):
        ran = range(-Hex.BOARD_SIZE, Hex.BOARD_SIZE + 1)
        return (-q-r in ran \
               and -Hex.BOARD_SIZE <= q <= Hex.BOARD_SIZE \
               and - Hex.BOARD_SIZE <= r <= Hex.BOARD_SIZE)  #coordinate equal to exit piece


    def __eq__(self, other):
        return self._q == other.q() and self._r == other.r()

    def __lt__(self, other):
        return self._q < other.q() or (self._q == other.q() and self._r < other.r())

    def __gt__(self, other):
        return self._q > other.q() or (self._q == other.q() and self._r > other.r())

    def copy(self):
        return Hex(self._q, self._r, self._type)