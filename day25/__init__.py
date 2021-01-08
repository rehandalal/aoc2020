from puzzle import Puzzle


class P1(Puzzle):
    test_result = 14897079

    def parse(self, data):
        return [int(d) for d in data.strip("\n").splitlines()]

    def transform(self, value, subject):
        value *= subject
        value %= 20201227
        return value

    def solve(self, data):
        loop_sizes = []

        for pk in data:
            loop_sizes.append(0)
            value = 1
            while value != pk:
                value = self.transform(value, 7)
                loop_sizes[-1] += 1

        ek = 1
        for _ in range(loop_sizes[0]):
            ek = self.transform(ek, data[1])
        return ek


class P2(P1):
    test_result = None
