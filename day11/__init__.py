from puzzle import Puzzle


class P1(Puzzle):
    test_result = 37
    tolerance = 4
    visibility = None

    def parse(self, data):
        return [[c for c in d.strip("\n")] for d in data.strip("\n").splitlines()]

    def count_occupied(self, data, x, y):
        visibility = self.visibility
        if visibility is None:
            visibility = {
                y: {
                    x: [
                        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                        (x - 1, y), (x + 1, y),
                        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                    ]
                }
            }
        count = 0

        for i, j in visibility[y][x]:
            if 0 <= i < len(data[0]) and 0 <= j < len(data) and data[j][i] == "#":
                count += 1

        return count

    def modify(self, data):
        modified = [d[:] for d in data]
        for y in range(len(data)):
            for x in range(len(data[y])):
                s = data[y][x]
                if s == ".":
                    continue
                count = self.count_occupied(data, x, y)
                if s == "L" and count == 0:
                    modified[y][x] = "#"
                elif s == "#" and count >= self.tolerance:
                    modified[y][x] = "L"
        return modified

    def solve(self, data):
        modified = self.modify(data)
        while data != modified:
            data = [d[:] for d in modified]
            modified = self.modify(data)

        count = 0
        for d in data:
            for s in d:
                if s == "#":
                    count += 1
        return count


class P2(P1):
    test_result = 26
    tolerance = 5

    def get_visibility(self, data, x, y):
        v = []
        delta = (
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1),
        )

        for dx, dy in delta:
            i, j = x + dx, y + dy
            while 0 <= i < len(data[0]) and 0 <= j < len(data):
                if data[j][i] != ".":
                    v.append((i, j))
                    break
                i += dx
                j += dy
        return v

    def solve(self, data):
        self.visibility = []
        for y in range(len(data)):
            self.visibility.append([])
            for x in range(len(data[y])):
                if data[y][x] == ".":
                    self.visibility[y].append([])
                    continue
                self.visibility[y].append(self.get_visibility(data, x, y))
        return super().solve(data)