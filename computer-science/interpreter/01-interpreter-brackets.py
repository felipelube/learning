from typing import Optional


EOF, L_PAREN, R_PAREN, L_SQUARE, R_SQUARE, L_CURLY, R_CURLY = 'EOF', 'L_PAREN', 'R_PAREN', 'L_SQUARE', 'R_SQUARE', 'L_CURLY', 'R_CURLY'
TOKEN_KIND_FOR_SYMBOL = {
    '(': L_PAREN,
    ')': R_PAREN,
    '[': L_SQUARE,
    ']': R_SQUARE,
    '{': L_CURLY,
    '}': R_CURLY
}


class Token:
    def __init__(self, kind: str) -> None:
        self.kind = kind

    def __str__(self) -> str:
        return f"Token ({self.kind})"

    def __repr__(self) -> str:
        return self.__str__()


class Interpreter:
    def __init__(self, text: str):
        self.text = text

        self.pos = 0
        self.token: Optional[Token] = None

    @property
    def current_char(self) -> Optional[str]:
        try:
            return self.text[self.pos]
        except IndexError:
            return None

    def advance(self):
        self.pos += 1

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            return Token(EOF)

        try:
            if self.current_char is None:
                raise
            kind = TOKEN_KIND_FOR_SYMBOL.get(self.current_char)
            self.advance()
            return Token(kind)
        except KeyError:
            raise Exception("Invalid token")


interpreter = Interpreter("()[]{}")

assert(interpreter.current_char == '(')
assert(interpreter.get_next_token().kind == L_PAREN)
assert(interpreter.current_char == ')')
assert(interpreter.get_next_token().kind == R_PAREN)

assert(interpreter.current_char == '[')
assert(interpreter.get_next_token().kind == L_SQUARE)
assert(interpreter.current_char == ']')
assert(interpreter.get_next_token().kind == R_SQUARE)

assert(interpreter.current_char == '{')
assert(interpreter.get_next_token().kind == L_CURLY)
assert(interpreter.current_char == '}')
assert(interpreter.get_next_token().kind == R_CURLY)

assert(interpreter.current_char is None)
assert(interpreter.get_next_token().kind == EOF)
