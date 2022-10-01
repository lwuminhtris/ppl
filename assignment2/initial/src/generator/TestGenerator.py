from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from BKITLexer import BKITLexer
from BKITParser import BKITParser
from ASTGeneration import ASTGeneration
from lexererr import *


class TestGenerator:
    @staticmethod
    def create():
        data_stream = TestGenerator.load()
        lexer = BKITLexer(data_stream)
        tokens = CommonTokenStream(lexer)
        parser = BKITParser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        print(asttree.__repr__())

    @staticmethod
    def load():
        data_stream = FileStream("PlainText.txt", "utf-8")
        return data_stream


TestGenerator.create()
