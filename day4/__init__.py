import re

from puzzle import Puzzle


def validate_year(low, high):
    def validator(value):
        return low <= value <= high
    return validator


def validate_height(value):
    details = re.findall("^([0-9]+?)(cm|in)$", value)
    if len(details) != 1:
        return False
    height, unit = details[0]
    try:
        if unit == "cm":
            return 150 <= int(height) <= 193
        else:
            return 59 <= int(height) <= 76
    except:
        return False


def validate_hcl(value):
    m = re.findall("^#[0-9a-f]{6}$", value)
    return len(m) == 1


def validate_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(value):
    m = re.findall("^[0-9]{9}$", value)
    return len(m) == 1


REQUIRED_FIELDS = [
    ("byr", int, validate_year(1920, 2002)),
    ("iyr", int, validate_year(2010, 2020)),
    ("eyr", int, validate_year(2020, 2030)),
    ("hgt", str, validate_height),
    ("hcl", str, validate_hcl),
    ("ecl", str, validate_ecl),
    ("pid", str, validate_pid)
]


class P1(Puzzle):
    test_result = 2

    def parse(self, data):
        return data.split("\n\n")

    def predicate(self, **kwargs):
        key = kwargs.get("key")
        data = kwargs.get("data")
        return key not in data

    def solve(self, data):
        count = len(data)
        for p in data:
            data = {}
            fields = re.findall(r"(.+?):(.+?)(?: |$|\n)", p)
            for key, value in fields:
                data[key] = value
            for key, cast, validate in REQUIRED_FIELDS:
                if self.predicate(key=key, data=data, cast=cast, validate=validate):
                    count -= 1
                    break
        return count


class P2(P1):
    test_result = 2

    def predicate(self, **kwargs):
        key = kwargs.get("key")
        data = kwargs.get("data")
        validate = kwargs.get("validate")
        cast = kwargs.get("cast")
        if key not in data:
            return True
        fv = cast(data[key])
        return not validate(fv)
