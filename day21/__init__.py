import re

from puzzle import Puzzle


class P1(Puzzle):
    test_result = 5

    def parse(self, data):
        allergens = {}
        ingredients = []
        for d in data.strip("\n").splitlines():
            matches = re.match(r"^(.+?) \(contains (.+?)\)", d)
            items = matches[1].split(" ")
            contains = matches[2].split(", ")
            for c in contains:
                if not c in allergens:
                    allergens[c] = []
                allergens[c].append(set(items))
            ingredients += items
        return allergens, ingredients

    def get_contaminated(self, allergens):
        contaminated = {}
        while len(contaminated) < len(allergens):
            for allergen in allergens:
                ingredients = allergens[allergen]
                ingredient = ingredients[0]
                for i in allergens[allergen]:
                    ingredient = ingredient.intersection(i)
                ingredient = ingredient.difference(set(contaminated.values()))
                if len(ingredient) == 1:
                    contaminated[allergen] = ingredient.pop()
        return contaminated

    def solve(self, data):
        allergens, ingredients = data
        contaminated = set(self.get_contaminated(allergens).values())
        safe = list(filter(lambda x: x not in contaminated, ingredients))
        return len(safe)


class P2(P1):
    test_result = "mxmxvkd,sqjhc,fvjkl"

    def solve(self, data):
        contaminated = self.get_contaminated(data[0])
        tainted = []
        for allergen in sorted(contaminated.keys()):
            tainted.append(contaminated[allergen])
        return ",".join(tainted)
