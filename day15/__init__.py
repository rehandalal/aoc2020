from puzzle import Puzzle


class P1(Puzzle):
    test_result = 436
    milestone = 2020

    def parse(self, data):
        parsed = [None] * self.milestone
        for i, d in enumerate(data.strip("\n").split(",")):
            parsed[i] = int(d)
        return parsed

    def solve(self, data):
        last_spoken = {}
        for i in range(self.milestone - 1):
            j = i + 1
            if data[j] is None:
                last = last_spoken.get(data[i], 0)
                data[j] = j - last if last > 0 else 0
            last_spoken[data[i]] = j
        return data[-1]


class P2(P1):
    test_result = None
    milestone = 30000000

