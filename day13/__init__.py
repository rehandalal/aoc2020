from puzzle import Puzzle


class P1(Puzzle):
    test_result = 295
    ts = 0

    def parse(self, data):
        data = data.strip("\n").splitlines()
        self.ts = int(data[0])
        return [id.strip("\n") if id.startswith("x") else int(id) for id in data[1].split(",")]

    def solve(self, data):
        minwait = None
        bus_id = None
        for b in data:
            if b == "x":
                continue
            wait = b - (self.ts % b)
            if minwait is None or wait < minwait:
                minwait = wait
                bus_id = b

        return minwait * bus_id


class P2(P1):
    test_result = 1068781

    def solve(self, data):
        ts = 0
        step = 1
        for wait, bus_id in enumerate(data):
            if bus_id == "x":
                continue
            while (ts + wait) % bus_id:
                ts += step
            step *= bus_id
        return ts
