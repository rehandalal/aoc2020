from puzzle import Puzzle


class P1(Puzzle):
    test_result = 7

    def parse(self, data):
        return [[c for c in d] for d in data.strip("\n").splitlines()]

    def count_trees(self, sx, sy, matrix):
        px, py, count = 0, 0, 0

        while py < len(matrix) - sy:
            py += sy
            px = (px + sx) % len(matrix[0])
            if matrix[py][px] == "#":
                count += 1

        return count

    def solve(self, data):
        return self.count_trees(3, 1, data)


class P2(P1):
    test_result = 336

    def solve(self, data):
        t1 = self.count_trees(1, 1, data)
        t2 = self.count_trees(3, 1, data)
        t3 = self.count_trees(5, 1, data)
        t4 = self.count_trees(7, 1, data)
        t5 = self.count_trees(1, 2, data)
        return t1 * t2 * t3 * t4 * t5
