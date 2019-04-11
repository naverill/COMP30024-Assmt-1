import heapq


class PriorityQueue:
    def __init__(self):
        self._elements = []

    def empty(self):
        return len(self._elements) == 0

    def put(self, item, priority):
        heapq.heappush(self._elements, (priority, item))

    def get(self):
        return heapq.heappop(self._elements)[1]

    def len(self):
        return len(self._elements)

    def __contains__(self, other):
        for item in self._elements:
            if other == item[1]:
                return True
        return False

    def __index__(self, i):
        return self._elements[i][1]

    def index(self, item):
        for index, elem in enumerate(self._elements):
            if item == elem[1]:
                return index
        return -1


