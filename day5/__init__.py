from puzzle import Puzzle


class P1(Puzzle):
    test_result = 357

    def parse(self, data):
        return data.strip("\n").splitlines()

    def get_seat_ids(self, data):
        seat_ids = []

        for d in data:
            low, high = 0, 127

            for i in range(6):
                mid = ((high - low) // 2) + 1
                if d[i] == "F":
                    high -= mid
                else:
                    low += mid

            row = low if d[6] == "F" else high

            low, high = 0, 7

            for i in range(2):
                mid = ((high - low) // 2) + 1
                if d[7 + i] == "L":
                    high -= mid
                else:
                    low += mid

            col = low if d[9] == "L" else high

            seat_id = (row * 8) + col
            seat_ids.append(seat_id)

        return seat_ids

    def solve(self, data):
        return max(self.get_seat_ids(data))


class P2(P1):
    test_result = None

    def solve(self, data):
        seat_ids = self.get_seat_ids(data)
        for i in range((127 * 8) + 7):
            if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
                return i
