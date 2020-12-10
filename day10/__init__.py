from puzzle import Puzzle


class P1(Puzzle):
    test_result = 35

    def parse(self, data):
        data = sorted([int(d) for d in data.strip("\n").splitlines()])
        final = max(data) + 3
        return [0] + data + [final]

    def solve(self, data):
        count_d1, count_d3 = 0, 0
        for i in range(1, len(data)):
            diff = data[i] - data[i - 1]
            if diff == 1:
                count_d1 += 1
            elif diff == 3:
                count_d3 += 1

        return count_d1 * count_d3


class P2(P1):
    test_result = 8

    def numWays(self, data, i=0, cache=None):
        if cache is None:
            cache = {}

        if i == len(data) - 1:
            cache[i] = 1

        if i in cache:
            return cache[i]

        ways = 0
        if len(data) > i + 1 and data[i + 1] - data[i] <= 3:
            ways += self.numWays(data, i + 1, cache)
        if len(data) > i + 2 and data[i + 2] - data[i] <= 3:
            ways += self.numWays(data, i + 2, cache)
        if len(data) > i + 3 and data[i + 3] - data[i] <= 3:
            ways += self.numWays(data, i + 3, cache)

        cache[i] = ways
        return ways

    def solve(self, data):
        return self.numWays(data)
