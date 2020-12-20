import regex
from puzzle import Puzzle


class P1(Puzzle):
    test_result = 3

    def __init__(self, *args, **kwargs):
        self.rules = {}
        super().__init__(*args, **kwargs)

    def parse(self, data):
        ruleset, messages = [d.splitlines() for d in data.strip("\n").split("\n\n")]
        rules = {}
        for r in ruleset:
            matches = regex.match(r"([0-9]+?): (.+?)$", r)
            id = int(matches[1])
            rulegroups = matches[2]
            if rulegroups.startswith('"'):
                rules[id] = rulegroups[1]
            else:
                rules[id] = [[int(g) for g in group.split(" ")] for group in rulegroups.split(" | ")]
        return rules, messages

    def compile(self, id):
        groups = self.rules[id]
        if isinstance(groups, str):
            return groups
        group_exprs = []
        for group in groups:
            expr = ""
            for rule_id in group:
                expr += self.compile(rule_id)
            group_exprs.append(expr)
        compiled = f"(?:{'|'.join(group_exprs)})"
        self.rules[id] = compiled
        return compiled

    def solve(self, data):
        self.rules, messages = data
        pattern = f"^{self.compile(0)}$"
        count = 0
        for m in messages:
            if regex.match(pattern, m):
                count += 1
        return count


class P2(P1):
    test_result = 12

    def compile(self, id):
        compiled = super().compile(id)
        if id == 8:
            return f"{compiled}+"
        if id == 11:
            c42 = super().compile(42)
            c31 = super().compile(31)
            return f"({c42}(?1)*{c31})"
        return compiled
