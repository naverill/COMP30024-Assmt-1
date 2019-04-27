from move import Move
from priority_queue import PriorityQueue
import search


class AStar:
    """
    Implementation of the search algorithm AStar to return an optimal path from the player pieces to the goal tile
    @param board_dict   : dictionary mapping coordinates to  all non-player tiles on the board
    @param start_hexs   : dictionary mapping coordinates to starting positions for all player positions on the board
    @param goal_hexs    : dictionary mapping coordinates to all goal hexs for the current player
    @param obstacles    : list of types for all obstacles on the board
    """
    def __init__(self, board_dict, start_hexs, goal_hexs, obstacles):
        self._empty_board = board_dict
        self._start = start_hexs
        self._goals = goal_hexs
        self._obstacles = obstacles

    """
    Method to return optimal path to the goal tiles
    @return list of moves from starting positions to goal tiles 
    """
    def search(self):
        # set the first node as the starting positions of all pieces
        start = Move(None, self._start, self._goals)
        # G cost of starting node is zero
        start.set_g(0)
        # find the initial h cost
        start.set_h()

        frontier = PriorityQueue()  # unexplored nodes
        explored = set()  # explored nodes

        frontier.put(start, start.f())  # begin by exploring first node

        # loop until no more nodes left to explore
        while not frontier.empty():
            curr_move = frontier.get()  # get node to be expanded, according to f cost
            explored.add(curr_move)  # add node to be expanded in explored

            if curr_move.end():  # if goal is found break out of loop
                break
            # update the board to include current positions of all pieces on board
            board_state = self.update_board(curr_move.state().values())
            # get the valid neighbouring tiles
            children = curr_move.get_children(board_state, self._obstacles)

            for child in children:
                # check if node hasn't already been expanded
                if child in explored:
                    continue

                child.set_g(curr_move.g() + child.cost)
                child.set_h()

                if child in frontier:
                    # if equivalent explored node has lower path cost, ignore current node
                    if child.g() > frontier.get(child).g():
                        continue
                # add low g cost, unexplored neighbour
                frontier.put(child, child.f())

        path = []
        current = curr_move
        while current is not None:
            path.append(current)
            current = current.parent()
        # reverse path
        return path[::-1]

    """
    Method to update empty board dict with current player piece positions
    @param state : dict mapping coordinates to current player positions 
    @return      : dict mapping coordinates to all hexs on the board
    """
    def update_board(self, state):
        board = {key: value.copy() for key, value in self._empty_board.items()}

        for hex in state:
            board[hex.get_coordinate()] = hex

        return board
