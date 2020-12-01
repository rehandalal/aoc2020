#!/usr/bin/env python

import importlib
import os
import sys


ROOT = os.path.abspath(os.path.dirname(__file__))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    day = sys.argv[2] if len(sys.argv) > 2 else ""

    if cmd not in ["run", "test"]:
        print("Invalid command. Try `run` or `test`.")
        exit(1)

    if not day:
        print(f"Select a day to {cmd}.")
        exit(1)

    if not os.path.exists(os.path.join(ROOT, f"day{day}")):
        print("Invalid day.")
        exit(1)

    module = importlib.import_module(f"day{day}")

    with open(os.path.join(ROOT, f"day{day}", "input.txt")) as f:
        input = f.read()

    with open(os.path.join(ROOT, f"day{day}", "test.txt")) as f:
        test_data = f.read()

    part1 = module.P1(input, test_data)
    part2 = module.P2(input, test_data)

    if cmd == "run":
        result = part1.run()
        print(f"> PART 1: {result}")
        result = part2.run()
        print(f"> PART 2: {result}")
    else:
        if part1.test_result is None:
            print("")
            print("Test not configured for PART 1.")
        else:
            print("")
            print("#" * 12)
            print("#  PART 1  #")
            print("#" * 12)
            part1.test()
        if part2.test_result is None:
            print("")
            print("Test not configured for PART 2.")
        else:
            print("")
            print("#" * 12)
            print("#  PART 2  #")
            print("#" * 12)
            part2.test()
        print("")
