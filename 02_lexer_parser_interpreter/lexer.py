class LexicalError(Exception):
    pass


class TokenType:
    INTEGER = "INTEGER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"  # End of input


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Move the 'pointer' to the next character in the input string."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer that breaks the input string into tokens."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MUL, "*")

            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIV, "/")

            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")")

            raise LexicalError("Lexical error")

        return Token(TokenType.EOF, None)
