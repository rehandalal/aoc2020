from puzzle import Puzzle


MAPPING = {
    "ne": (-0.5, -1),
    "nw": (0.5, -1),
    "w": (1, 0),
    "sw": (0.5, 1),
    "se": (-0.5, 1),
    "e": (-1, 0),
}


class P1(Puzzle):
    test_result = 10

    def plot(self, string):
        directions = []
        while len(string):
            if string.startswith("s") or string.startswith("n"):
                directions.append(string[:2])
                string = string[2:]
            else:
                directions.append(string[:1])
                string = string[1:]
        return directions

    def parse(self, data):
        return [self.plot(d) for d in data.strip("\n").splitlines()]

    def traverse(self, directions):
        reference = [0, 0]
        for d in directions:
            for i, o in enumerate(MAPPING[d]):
                reference[i] += o
        return tuple(reference)

    def get_black_tiles(self, data):
        blacks = set()
        for d in data:
            coords = self.traverse(d)
            if coords in blacks:
                blacks.discard(coords)
            else:
                blacks.add(coords)
        return blacks

    def solve(self, data):
        return len(self.get_black_tiles(data))


class P2(P1):
    test_result = 2208

    def get_neighbours(self, tile):
        neighbours = []
        for d in MAPPING:
            n = [tile[0], tile[1]]
            for i, o in enumerate(MAPPING[d]):
                n[i] += o
            neighbours.append(tuple(n))
        return neighbours

    def cycle(self, blacks):
        cycled = set()
        for t in blacks:
            count = 0
            for n in self.get_neighbours(t):
                if n in blacks:
                    count += 1
                else:
                    a_count = 0
                    for a in self.get_neighbours(n):
                        if a in blacks:
                            a_count += 1
                    if a_count == 2:
                        cycled.add(n)
            if 0 < count < 3:
                cycled.add(t)
        return cycled

    def solve(self, data):
        blacks = self.get_black_tiles(data)
        for _ in range(100):
            blacks = self.cycle(blacks)
        return len(blacks)
