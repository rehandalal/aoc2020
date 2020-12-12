from puzzle import Puzzle


DIRECTIONS = ["E", "S", "W", "N"]


class P1(Puzzle):
    test_result = 25

    def parse(self, data):
        return [[d[0], int(d[1:])] for d in data.strip("\n").splitlines()]

    def solve(self, data):
        dir = 0
        x = 0
        y = 0

        for inst, val in data:
            if inst == "F":
                inst = DIRECTIONS[dir]
            elif inst == "R":
                dir = (dir + (val // 90)) % 4
            elif inst == "L":
                dir = (dir - (val // 90)) % 4

            if inst == "E":
                x += val
            elif inst == "W":
                x -= val
            elif inst == "N":
                y += val
            elif inst == "S":
                y -= val

        return abs(x) + abs(y)


class P2(P1):
    test_result = 286

    def solve(self, data):
        wx = 10
        wy = 1
        x = 0
        y = 0
        for inst, val in data:
            if inst == "F":
                x += wx * val
                y += wy * val
            elif inst == "R" or inst == "L":
                dir = -1 if inst == "L" else 1
                deg = ((val // 90) * dir) % 4
                if deg == 1:
                    wx, wy = wy, -wx
                elif deg == 2:
                    wx, wy = -wx, -wy
                elif deg == 3:
                    wx, wy = -wy, wx
            elif inst == "E":
                wx += val
            elif inst == "W":
                wx -= val
            elif inst == "N":
                wy += val
            elif inst == "S":
                wy -= val
        return abs(x) + abs(y)
