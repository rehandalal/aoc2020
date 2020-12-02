from puzzle import Puzzle


class P1(Puzzle):
    test_result = 2

    def parse(self, data):
        return data.strip("\n").splitlines()

    def predicate(self, **kwargs):
        count = kwargs.get("count")
        low = kwargs.get("low")
        high = kwargs.get("high")
        return low <= count <= high

    def solve(self, data):
        valid = 0
        for d in data:
            policy, password = d.split(": ", 1)
            len_range, letter = policy.split(" ", 1)
            low, high = [int(n) for n in len_range.split("-", 1)]
            count = 0
            for p in password:
                if p == letter:
                    count += 1
            if self.predicate(count=count, low=low, high=high, password=password, letter=letter):
                valid += 1
        return valid


class P2(P1):
    test_result = 1

    def predicate(self, **kwargs):
        low = kwargs.get("low")
        high = kwargs.get("high")
        password = kwargs.get("password")
        letter = kwargs.get("letter")
        return (
            password[low - 1] != password[high - 1] and
            (password[low - 1] == letter or password[high - 1] == letter)
        )
