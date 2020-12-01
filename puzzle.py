class Puzzle(object):
    test_result = None

    def __init__(self, input, test_data):
        self.input = self.parse(input)
        self.test_data = self.parse(test_data)

    def parse(self, data):
        raise NotImplementedError("You must implement this method.")

    def solve(self, data):
        raise NotImplementedError("You must implement this method.")

    def run(self):
        return self.solve(self.input)

    def test(self):
        result = self.solve(self.test_data)
        if result == self.test_result:
            print("✅ Success!")
        else:
            print("❌ Failure!")
        print(f"Expected: {self.test_result}")
        print(f"Actual: {result}")
