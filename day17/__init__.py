from puzzle import Puzzle


class P1(Puzzle):
    test_result = 112
    dimensions = 3

    def parse(self, data):
        return [[c for c in d] for d in data.strip("\n").splitlines()]

    def construct(self, data):
        constructed = {}
        for y in range(len(data)):
            for x in range(len(data[0])):
                coords = [0] * (self.dimensions - 2)
                coords += [y, x]
                if data[y][x] == "#":
                    constructed[tuple(coords)] = True
        return constructed

    def get_neighbours(self, coords):
        neighbours = []
        for i in range(3 ** self.dimensions):
            tmp = [None] * self.dimensions
            for j in range(self.dimensions):
                tmp[j] = coords[j] + (i % 3) - 1
                i = i // 3
            neighbours.append(tuple(tmp))
        neighbours.remove(coords)
        return neighbours

    def cycle(self, matrix):
        updated = {}
        for point in matrix:
            neighbours = self.get_neighbours(point)
            active_neighbours = 0
            for n in neighbours:
                if matrix.get(n):
                    active_neighbours += 1
                adjacent = self.get_neighbours(n)
                active_adjacent = 0
                for a in adjacent:
                    if matrix.get(a):
                        active_adjacent += 1
                if active_adjacent == 3:
                    updated[n] = True
            if 2 <= active_neighbours <= 3:
                updated[point] = True
        return updated

    def solve(self, data):
        matrix = self.construct(data)
        for i in range(6):
            matrix = self.cycle(matrix)
        return len(matrix.keys())


class P2(P1):
    test_result = 848
    dimensions = 4
