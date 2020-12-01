from puzzle import Puzzle


class P1(Puzzle):
    test_result = 514579
    sum = 2020

    def parse(self, data):
        return [int(d) for d in data.strip("\n").splitlines()]

    def solve(self, data):
        cache = {}
        for d in data:
            cache[d] = self.sum - d
            if cache[d] in cache:
                return d * cache[d]


class P2(P1):
    test_result = 241861950

    def solve(self, data):
        for d in data:
            self.sum = super().sum - d
            complement = super().solve(data)
            if complement:
                return d * complement
