from lib2to3.pgen2.tokenize import TokenError
from typing import Optional, Union

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

TOKEN_TESTS = {
    INTEGER: lambda x: x.isdigit(),
    PLUS: lambda x: x == '+',
    MINUS: lambda x: x == '-',
    EOF: lambda x: x is None
}


class Token:
    def __init__(self, kind: str, value: Union[int, str, None]):
        self.kind = kind
        self.value = value

    def __str__(self) -> str:
        return f"Token ({self.kind}: {self.value})"


class Interpreter:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_token: Optional[Token] = None

    @property
    def current_char(self):
        try:
            return self.text[self.pos]
        except IndexError:
            return None

    def advance(self):
        self.pos += 1

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)

        while self.text[self.pos].isspace():
            self.advance()
            return self.get_next_token()

        for token_kind, test in TOKEN_TESTS.items():
            if test(self.current_char):
                token = Token(token_kind, self.current_char)
                self.advance()
                return token
        else:
            raise ValueError('Unidentified token')

    def eat(self, expected_kind):
        if self.current_token.kind == expected_kind:
            self.current_token = self.get_next_token()
        else:
            raise ValueError('Unexpected token')

    def expr(self, result=None):
        if result is not None:
            left = result
        else:
            self.current_token = self.get_next_token()
            left = self.current_token
            self.eat(INTEGER)

        op = self.current_token
        if op.kind == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.kind == PLUS:
            result = int(left.value) + int(right.value)
        else:
            result = int(left.value) - int(right.value)

        if self.current_token.kind != EOF:
            result = self.expr(Token(INTEGER, result))

        return result


interpreter = Interpreter("2 + 5")
assert(interpreter.expr() == 7)

interpreter = Interpreter("2 + 5 - 3 + 3")
assert(interpreter.expr() == 7)
