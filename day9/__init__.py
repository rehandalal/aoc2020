from puzzle import Puzzle


class P1(Puzzle):
    test_result = 127

    def parse(self, data):
        return [int(d) for d in data.strip("\n").splitlines()]

    def solve(self, data):
        preamble = 25 if len(data) > 25 else 5
        for i in range(preamble, len(data)):
            valid = False
            for j in range(i - preamble, i):
                diff = data[i] - data[j]
                if diff in data[i - preamble:i]:
                    valid = True
                    break
            if valid:
                continue
            else:
                return data[i]


class P2(P1):
    test_result = 62

    def solve(self, data):
        weak = super().solve(data)
        x, y = 0, 1
        sum = data[x] + data[y]

        while sum != weak:
            if sum < weak:
                y += 1
                sum += data[y]
            elif sum > weak:
                sum -= data[x]
                x += 1
        y += 1

        return min(data[x:y]) + max(data[x:y])
