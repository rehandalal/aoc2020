from puzzle import Puzzle


class P1(Puzzle):
    test_result = 67384529
    rounds = 100

    def parse(self, data):
        return [int(d) for d in data.strip("\n")]

    def move(self, curr, mapping):
        pickup = [mapping[curr]]
        pickup.append(mapping[pickup[-1]])
        pickup.append(mapping[pickup[-1]])
        nxt = mapping[pickup[-1]]

        dest = curr - 1
        while dest in pickup or dest < 1:
            if dest < 1:
                dest = max(mapping)
            else:
                dest -= 1

        mapping[curr] = nxt
        mapping[pickup[2]] = mapping[dest]
        mapping[dest] = pickup[0]
        return nxt

    def answer(self, mapping):
        ans = []
        curr = 1
        nxt = mapping[curr]
        while nxt != 1:
            ans.append(nxt)
            curr = nxt
            nxt = mapping[curr]
        return int("".join([str(d) for d in ans]))

    def solve(self, data):
        mapping = {}
        for i, d in enumerate(data):
            mapping[d] = data[(i + 1) % len(data)]
        curr = data[0]
        for _ in range(self.rounds):
            curr = self.move(curr, mapping)
        return self.answer(mapping)


class P2(P1):
    test_result = 149245887792
    rounds = 10_000_000

    def parse(self, data):
        data = super().parse(data)
        for i in range(max(data), 1_000_000):
            data.append(i + 1)
        return data

    def answer(self, mapping):
        p1 = mapping[1]
        p2 = mapping[p1]
        return p1 * p2
