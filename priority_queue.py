import heapq


class PriorityQueue:
    def __init__(self):
        self._elements = []

    def empty(self):
        return len(self._elements) == 0

    def put(self, item, priority):
        heapq.heappush(self._elements, (priority, item))

    def get(self, state=None):
        if state:
            index = self.index(state)
            return self._elements[index][1]
        return heapq.heappop(self._elements)[1]

    def len(self):
        return len(self._elements)

    def __contains__(self, other):
        for item in self._elements:
            if other == item[1]:
                return True
        return False

    def index(self, item):
        for index, elem in enumerate(self._elements):
            if item == elem[1]:
                return index
        return -1

    def remove(self, item):
        index = self.index(item)
        self._elements.pop(index)

    def print_costs(self):
        for item in self._elements:
            print(item[0], item[1].f())
        print()

