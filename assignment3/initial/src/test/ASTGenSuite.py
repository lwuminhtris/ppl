import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {}"""
        input = """
        Function: main
        Body:
            foo();
        EndBody.
        """
        expect = str(Program([VarDecl(Id("x"), [], None)]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    # def test_more_complex_program(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Body:
    #         x = 10;
    #         printLn(x);
    #     EndBody.
    #     """
    #     expect = str(Program([
    #         VarDecl(Id("x"),[],IntLiteral(5)),
    #         FuncDecl(Id("main"),[],([],[
    #             Assign(Id("x"),IntLiteral(10)),
    #             CallStmt(Id("printLn"),[Id("x")])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))


# Tuple (,)=> record (Pascal), struct [0]  [1]
