
class LexerError(Exception):
    pass

class ErrorToken(LexerError):
    def __init__(self,s):
        self.message = "Error Token "+ s

class UncloseString(LexerError):
    def __init__(self,s):
        self.message = "Unclosed String: "+ s

class IllegalEscape(LexerError):
    def __init__(self,s):
        self.message = "Illegal Escape In String: "+ s

class UnterminatedComment(LexerError):
    def __init__(self):
        self.message = "Unterminated Comment"



