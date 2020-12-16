from puzzle import Puzzle


class P1(Puzzle):
    test_result = 436
    milestone = 2020

    def parse(self, data):
        return [int(d) for d in data.strip("\n").split(",")]

    def solve(self, data):
        last_spoken = {}
        for i, h in enumerate(data):
            last_spoken[h] = i + 1
        data.append(0)
        for i in range(len(data), self.milestone):
            prev = data[-1]
            if prev in last_spoken:
                data.append(len(data) - last_spoken[prev])
            else:
                data.append(0)
            last_spoken[prev] = i
        return data[-1]


class P2(P1):
    test_result = None
    milestone = 30000000

