import re

from puzzle import Puzzle


class P1(Puzzle):
    test_result = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = {}
        self.data = None
        self.acc, self.pos = 0, 0

    def parse(self, data):
        parsed = []
        for d in data.strip("\n").splitlines():
            c = re.match(r"(.{3}) \+?(-?[0-9]+)", d)
            parsed.append((c[1], int(c[2])))
        return parsed

    def operate(self, cmd, val):
        if self.pos in self.cache:
            return True
        self.cache[self.pos] = True
        if cmd == "nop":
            self.pos += 1
        elif cmd == "acc":
            self.acc += val
            self.pos += 1
        else:
            self.pos += val
        return False

    def solve(self, data):
        self.data = data
        complete = False
        while not complete:
            complete = self.operate(*data[self.pos])
        return self.acc


class P2(P1):
    test_result = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.altered = False

    def operate(self, cmd, val):
        if self.cache.get(self.pos, {}).get("seen", False):
            self.acc = 0
            for i in range(len(self.data)):
                if i not in self.cache:
                    self.cache[i] = {}
                self.cache[i]["seen"] = False
            self.pos = 0
            self.altered = False
            return False

        if self.pos not in self.cache:
            self.cache[self.pos] = {}
        self.cache[self.pos]["seen"] = True

        if not self.altered and not self.cache[self.pos].get("altered"):
            if cmd == "nop":
                cmd = "jmp"
            elif cmd == "jmp":
                cmd = "nop"
            self.altered = True
            self.cache[self.pos]["altered"] = True

        if cmd == "nop":
            self.pos += 1
        elif cmd == "acc":
            self.acc += val
            self.pos += 1
        else:
            self.pos += val

        if self.pos < len(self.data):
            return False
        return True
