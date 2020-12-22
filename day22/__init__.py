from collections import deque
from puzzle import Puzzle


class ShortCircuit(Exception):
    pass


class P1(Puzzle):
    test_result = 306

    def parse(self, data):
        return [deque([int(c) for c in d.strip("\n").splitlines()[1:]]) for d in data.split("\n\n")]

    def play_round(self, data, *args):
        p = [d.popleft() for d in data]
        w = 0 if p[0] > p[1] else 1
        data[w].append(p[w])
        data[w].append(p[1 - w])
        return w

    def play_game(self, data, *args):
        winner = None
        while len(data[0]) > 0 and len(data[1]) > 0:
            winner = self.play_round(data, *args)
        return winner

    def solve(self, data, *args):
        winner = self.play_game(data, *args)
        total = 0
        for i, n in enumerate(data[winner]):
            total += (len(data[winner]) - i) * n
        return total


class P2(P1):
    test_result = 291

    def solve(self, data, *args):
        return super().solve(data, [])

    def hash(self, data):
        return f"0-{','.join([str(i) for i in data[0]])}::1-{','.join([str(i) for i in data[1]])}"

    def play_game(self, data, *args):
        try:
            return super().play_game(data, *args)
        except ShortCircuit:
            return 0

    def play_round(self, data, *args):
        cache = args[0]
        if self.hash(data) in cache:
            raise ShortCircuit()
        cache.append(self.hash(data))
        p = [d.popleft() for d in data]
        if len(data[0]) and len(data[1]) and p[0] <= len(data[0]) and p[1] <= len(data[1]):
            subdata = [deque(list(d)[:p[i]]) for i, d in enumerate(data)]
            w = self.play_game(subdata, [])
            data[w].append(p[w])
            data[w].append(p[1 - w])
            return w
        else:
            data[0].appendleft(p[0])
            data[1].appendleft(p[1])
            return super().play_round(data)
