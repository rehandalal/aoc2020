import re

from puzzle import Puzzle


class P1(Puzzle):
    test_result = 4

    def parse(self, data):
        return data.strip("\n").splitlines()

    def has_target(self, bag, mapping, cache=None):
        if cache is None:
            cache = {}
        elif bag in cache:
            return cache[bag]

        if "shiny gold" in mapping[bag]:
            cache[bag] = True
            return True
        else:
            contains = False
            for nested in mapping[bag]:
                contains = contains or self.has_target(nested, mapping, cache)
            cache[bag] = contains
            return contains

    def count(self, mapping):
        count = 0
        for bag in mapping:
            mapping[bag] = [m[1] for m in mapping[bag]]
        for bag in mapping:
            if self.has_target(bag, mapping):
                count += 1
        return count

    def solve(self, data):
        mapping = {}

        for d in data:
            bag, contents = d.strip("\n").split(" contain ", 1)
            bag = re.match(r"(.+?) bags", bag)[1]
            if contents == "no other bags.":
                mapping[bag] = []
            else:
                types = re.findall(r"([0-9]+) (.+?) bags?(?:, |\.)", contents)
                mapping[bag] = types

        return self.count(mapping)


class P2(P1):
    test_result = 32

    def count_nested(self, bag, mapping, cache=None):
        if cache is None:
            cache = {}
        elif bag in cache:
            return cache[bag]

        count = 0
        for nested in mapping[bag]:
            count += nested[0] + (nested[0] * self.count_nested(nested[1], mapping, cache))
        cache[bag] = count
        return count

    def count(self, mapping):
        for bag in mapping:
            mapping[bag] = [(int(m[0]), m[1]) for m in mapping[bag]]
        return self.count_nested("shiny gold", mapping)
