from enum import Enum, auto

from puzzle import Puzzle


EQ_WHITESPACE = [" "]
EQ_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
EQ_PLUS = "+"
EQ_MULTIPLY = "*"
EQ_OPERATORS = [EQ_PLUS, EQ_MULTIPLY]
EQ_LPARENS = "("
EQ_RPARENS = ")"


class Token(Enum):
    EXP = auto()
    NUM = auto()
    OPR = auto()


class Node(object):
    def __init__(self, token, value=None):
        self.token = token
        self.value = value
        self.children = []

    def add(self, child):
        self.children.append(child)


class Lexer(object):
    def __init__(self, string):
        self.string = string

    def lex_expression(self, string):
        if string[0] == EQ_LPARENS:
            lp_count = 1
            rp_count = 0
            for i in range(1, len(string)):
                if string[i] == EQ_LPARENS:
                    lp_count += 1
                elif string[i] == EQ_RPARENS:
                    rp_count += 1
                    if lp_count == rp_count:
                        return Lexer(string[1:i]).lex(), string[i+1:]
            raise Exception(f"Expected `{EQ_RPARENS}`.")
        return None, string

    def lex_number(self, string):
        number = ""
        for char in string:
            if char not in EQ_NUMBERS:
                break
            number += char
        if number:
            return Node(Token.NUM, int(number)), string[len(number):]
        return None, string

    def lex(self):
        lexed = Node(Token.EXP)
        string = self.string
        while len(string):
            token, string = self.lex_expression(string)
            if token:
                lexed.add(token)

            token, string = self.lex_number(string)
            if token:
                lexed.add(token)

            if len(string) == 0:
                break

            char = string[0]

            if char in EQ_WHITESPACE:
                pass
            elif char == EQ_RPARENS:
                raise Exception(f"Unexpected character `{EQ_RPARENS}`.")
            elif char in EQ_OPERATORS:
                lexed.add(Node(Token.OPR, char))
            string = string[1:]
        return lexed


class LTRParser(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        value = None
        operator = None
        for node in self.tokens.children:
            if value is None and node.token == Token.OPR:
                raise Exception(f"Unexpected character `{node.value}`.")
            if node.token == Token.OPR:
                operator = node.value
            else:
                if node.token == Token.EXP:
                    node_value = LTRParser(node).parse()
                else:
                    node_value = node.value
                if value is None:
                    value = node_value
                elif operator == EQ_PLUS:
                    value += node_value
                else:
                    value *= node_value
        return value


class PPMParser(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        tokens = self.tokens.children[:]

        # Flatten
        for i in range(len(tokens)):
            node = tokens[i]
            if node.token == Token.EXP:
                tokens[i] = Node(Token.NUM, PPMParser(node).parse())

        tmp = []
        value = None
        for i in range(len(tokens)):
            node = tokens[i]
            if value is None and node.token == Token.OPR:
                raise Exception(f"Unexpected character `{node.value}`.")
            if node.token == Token.OPR and node.value == EQ_MULTIPLY:
                tmp.append(Node(Token.NUM, value))
                tmp.append(node)
                value = None
            if node.token == Token.NUM:
                if value is None:
                    value = node.value
                else:
                    value += node.value
        tmp.append(Node(Token.NUM, value))
        tokens = tmp

        value = None
        for i in range(len(tokens)):
            node = tokens[i]
            if node.token == Token.NUM:
                if value is None:
                    value = node.value
                else:
                    value *= node.value

        return value


class P1(Puzzle):
    test_result = 26457
    Parser = LTRParser

    def parse(self, data):
        return data.strip("\n").splitlines()

    def solve(self, data):
        total = 0
        for equation in data:
            tokens = Lexer(equation).lex()
            total += self.Parser(tokens).parse()
        return total


class P2(P1):
    test_result = 694173
    Parser = PPMParser
