
class Hex:
    """
    Class that defines a hex tile on the board
    @param q    : the q value of the hex
    @param r    : the r value of the hex
    @param type : the type of the hex
    """
    BOARD_SIZE = 3
    # defines a tile on the board
    def __init__(self, q=-1, r=-1, type=''):  # contains coordinates and type of tile
        self._q = q
        self._r = r
        self._type = type
        self._neighbours = [self.left, self.right, self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    """
    Method that returns if piece is valid
    @returns bool   : indicates if hex xcoordinate is valid 
    """
    @staticmethod
    def is_valid(q, r):  # checks if a certain coordinate is valid
        ran = range(-Hex.BOARD_SIZE, Hex.BOARD_SIZE + 1)
        return (-q - r in ran \
                and -Hex.BOARD_SIZE <= q <= Hex.BOARD_SIZE \
                and - Hex.BOARD_SIZE <= r <= Hex.BOARD_SIZE)

    """
    Method to return all valid neighbours of the current hex 
    @return     list containing all valid hexs 
    """
    def get_neighbours(self):
        neighbours = []
        for neighbour in self._neighbours:
            if neighbour():
                neighbours.append(neighbour())
        return neighbours

    """
    Method that finds tile opposite to given obstacle, assuming tiles are adjacent 
    @return     : valid tile as the result of a jump move 
    """
    def jump(self, obstacle, board):  # finds opposite tile and returns it if jump is possible
        opposite = self._opposite_neighbour(obstacle)

        if self.is_valid(opposite[0], opposite[1]):
            return board[opposite]
        else:
            return None

    """
    Method to get tile on the opposite side of neighbouring tile
    @param neighbour    : neighbour hex of current hex  
    @return    hex on opposite side of neighbour from current tile  
    """
    def _opposite_neighbour(self, neighbour):  # returns opposite tile for jumping
        dist_q = neighbour.q() - self.q()
        dist_r = neighbour.r() - self.r()
        return neighbour.q() + dist_q, neighbour.r() + dist_r

    """
    Method to return deep copy of hex tile
    @return copy of current tile 
    
    """
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

    """
    Method to return hex to the left of current hex
    @return coordinates of hex 
    """
    def left(self):  # returns left tile
        if not Hex.is_valid(self._q - 1, self._r):
            return None
        return self._q - 1, self._r

    """
    Method to return hex to the right of current hex
    @return coordinates of hex 
    """
    def right(self):  # returns right tile
        if not Hex.is_valid(self._q + 1, self._r):
            return None
        return self._q + 1, self._r

    """
    Method to return hex to the top left of current hex
    @return coordinates of hex 
    """
    def top_left(self):  # returns top left tile
        if not Hex.is_valid(self._q, self._r - 1):
            return None
        return self._q, self._r - 1

    """
    Method to return hex to the top right of current hex
    @return coordinates of hex 
    """
    def top_right(self):  # returns top right tile
        if not Hex.is_valid(self._q + 1, self._r - 1):
            return None
        return self._q + 1, self._r - 1

    """
    Method to return hex to the bottom left of current hex
    @return coordinates of hex 
    """
    def bottom_left(self):  # returns bottom left tile
        if not Hex.is_valid(self._q - 1, self._r + 1):
            return None
        return self._q - 1, self._r + 1

    """
    Method to return hex to the bottom right of current hex
    @return coordinates of hex 
    """
    def bottom_right(self):  # returns bottom right tile
        if not Hex.is_valid(self._q, self._r + 1):
            return None
        return self._q, self._r + 1

    """
    Method return boolean value if coordinates of hex tiles are equal
    @return boolean value
    """
    def __eq__(self, other):
        return self._q == other.q() and self._r == other.r()

    """
    Method return boolean value if current hex tiles is less than other tile
    @return boolean value
    """
    def __lt__(self, other):
        return self._q < other.q() or (self._q == other.q() and self._r < other.r())

    """
    Method return boolean value if current hex tiles is greater than other tile
    @return boolean value
    """
    def __gt__(self, other):
        return self._q > other.q() or (self._q == other.q() and self._r > other.r())
