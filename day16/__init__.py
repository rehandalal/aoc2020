import re

from puzzle import Puzzle


class P1(Puzzle):
    test_result = 71

    def __init__(self, *args, **kwargs):
        self.mine = []
        self.nearby = []
        self.ruleset = {}
        super().__init__(*args, **kwargs)

    def parse(self, data):
        return data.split("\n\n")

    def solve(self, data):
        self.mine = data[1].strip("\n").split("\n")[1].split(",")
        self.nearby = [d.split(",") for d in data[2].strip("\n").split("\n")[1:]]
        self.ruleset = {}
        for field, l1, u1, l2, u2 in re.findall(r"(.+?): ([0-9]+?)-([0-9]+?) or ([0-9]+?)-([0-9]+)", data[0]):
            self.ruleset[field] = (
                (int(l1), int(u1)),
                (int(l2), int(u2))
            )

        validated = []
        error_rate = 0
        for ticket in self.nearby:
            ticket_valid = True
            for field in ticket:
                field = int(field)
                field_valid = False
                for r1, r2 in self.ruleset.values():
                    if r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]:
                        field_valid = True
                        break
                if not field_valid:
                    ticket_valid = False
                    error_rate += field
            if ticket_valid:
                validated.append(ticket)

        self.nearby = validated
        return error_rate


class P2(P1):
    test_result = None

    def solve(self, data):
        super().solve(data)
        mapping = [list(self.ruleset.keys()) for i in range(len(self.nearby[0]))]
        for ticket in self.nearby:
            for i, field in enumerate(ticket):
                if len(mapping[i]) == 1:
                    continue
                field = int(field)
                bad = []
                for m in mapping[i]:
                    r1, r2 = self.ruleset[m]
                    if r1[0] <= field <= r1[1] or r2[0] <= field <= r2[1]:
                        continue
                    bad.append(m)
                for b in bad:
                    mapping[i].remove(b)

        for _ in range(len(mapping)):
            for i in range(len(mapping)):
                if len(mapping[i]) == 1:
                    for j in range(len(mapping)):
                        if j == i:
                            continue
                        if mapping[i][0] in mapping[j]:
                            mapping[j].remove(mapping[i][0])
                    continue

        answer = 1
        for i, m in enumerate(mapping):
            if m[0].startswith("departure"):
                answer *= int(self.mine[i])
        return answer
