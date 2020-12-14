import re

from puzzle import Puzzle


class P1(Puzzle):
    test_result = 51

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = {}

    def parse(self, data):
        return data.strip("\n").splitlines()

    def modify(self, pos, val, mask):
        b36 = bin(val).replace("0b", "").rjust(36, "0")
        masked = ""
        for i in range(36):
            if mask[i] == "X":
                masked += b36[i]
            else:
                masked += mask[i]
        self.memory[pos] = int(masked, 2)

    def solve(self, data):
        mask = "X" * 36
        for d in data:
            if d.startswith("mask"):
                mask = d[7:].strip("\n")
            else:
                match = re.match(r"^mem\[(.+?)] = (.+?)(?:\n|$)", d)
                pos = int(match[1])
                val = int(match[2])
                self.modify(pos, val, mask)

        total = 0
        for k in self.memory:
            total += self.memory[k]
        return total


class P2(P1):
    test_result = 208

    def modify(self, pos, val, mask):
        target = bin(pos).replace("0b", "").rjust(36, "0")
        values = [""]
        for cursor in range(36):
            next = mask[cursor]
            if next == "0":
                for i in range(len(values)):
                    values[i] += target[cursor]
            elif next == "1":
                for i in range(len(values)):
                    values[i] += "1"
            else:
                tmp = []
                for i in range(len(values)):
                    tmp.append(f"{values[i]}0")
                    tmp.append(f"{values[i]}1")
                values = tmp

        for p in values:
            self.memory[p] = val
