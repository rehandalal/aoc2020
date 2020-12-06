from puzzle import Puzzle


class P1(Puzzle):
    test_result = 11

    def parse(self, data):
        return data.split("\n\n")

    def process_people(self, people):
        answers = set()
        for person in people:
            for answer in person:
                answers.add(answer)
        return answers

    def solve(self, data):
        count = 0
        for group in data:
            people = group.splitlines(keepends=False)
            answers = self.process_people(people)
            count += len(answers)
        return count


class P2(P1):
    test_result = 6

    def process_people(self, people):
        answers = None
        for person in people:
            person_answers = set()
            for answer in person:
                person_answers.add(answer)
            if answers is None:
                answers = person_answers
            else:
                answers = answers.intersection(person_answers)
        return answers
