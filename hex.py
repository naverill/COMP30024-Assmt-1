
class Hex:
    BOARD_SIZE = 3
    # defines a tile on the board

    def __init__(self, q=-1, r=-1, type=''):  # contains coordinates and type of tile
        self._q = q
        self._r = r
        self._type = type
        self._neighbours = [self.left, self.right, self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    @staticmethod
    def is_valid(q, r):  # checks if a certain coordinate is valid
        ran = range(-Hex.BOARD_SIZE, Hex.BOARD_SIZE + 1)
        return (-q - r in ran \
                and -Hex.BOARD_SIZE <= q <= Hex.BOARD_SIZE \
                and - Hex.BOARD_SIZE <= r <= Hex.BOARD_SIZE)

    def get_neighbours(self):  # returns valid neighbours
        neighbours = []
        for neighbour in self._neighbours:
            if neighbour():
                neighbours.append(neighbour())
        return neighbours

    def jump(self, obstacle, board):  # finds opposite tile and returns it if jump is possible
        opposite = self._opposite_neighbour(obstacle)

        if self.is_valid(opposite[0], opposite[1]):
            return board[opposite]
        else:
            return None

    def _opposite_neighbour(self, neighbour):  # returns opposite tile for jumping
        dist_q = neighbour.q() - self.q()
        dist_r = neighbour.r() - self.r()
        return neighbour.q() + dist_q, neighbour.r() + dist_r

    def copy(self):
        return Hex(self._q, self._r, self._type)

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

    def left(self):  # returns left tile
        if not Hex.is_valid(self._q - 1, self._r):
            return None
        return self._q - 1, self._r

    def right(self):  # returns right tile
        if not Hex.is_valid(self._q + 1, self._r):
            return None
        return self._q + 1, self._r

    def top_left(self):  # returns top left tile
        if not Hex.is_valid(self._q, self._r - 1):
            return None
        return self._q, self._r - 1

    def top_right(self):  # returns top right tile
        if not Hex.is_valid(self._q + 1, self._r - 1):
            return None
        return self._q + 1, self._r - 1

    def bottom_left(self):  # returns bottom left tile
        if not Hex.is_valid(self._q - 1, self._r + 1):
            return None
        return self._q - 1, self._r + 1

    def bottom_right(self):  # returns bottom right tile
        if not Hex.is_valid(self._q, self._r + 1):
            return None
        return self._q, self._r + 1

    def __eq__(self, other):
        return self._q == other.q() and self._r == other.r()

    def __lt__(self, other):
        return self._q < other.q() or (self._q == other.q() and self._r < other.r())

    def __gt__(self, other):
        return self._q > other.q() or (self._q == other.q() and self._r > other.r())
