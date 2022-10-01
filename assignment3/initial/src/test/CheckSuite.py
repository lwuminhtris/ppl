import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_simple_function(self):
        """Simple program: main"""
        input = """
            Function: a
            Body:

            EndBody.

            Function: b
            Body:

            EndBody.
                """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_function(self):
        """Simple program: main"""
        input = """
            Function: main
            Body:

            EndBody.

            Function: main
            Body:

            EndBody.
                """
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_param_function(self):
        """Simple program: main"""
        input = """
            Function: main
            Parameter: a, b
            Body:
                Var: c, d;
                d = 1;
            EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_assign_function(self):
        """Simple program: main"""
        input = """
            Function: main
            Parameter: a, b
            Body:
                Var: c, d;
                d = c;
            EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("d"), Id("c"))))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_assign_function_2(self):
        """Simple program: main"""
        input = """
            Function: main
            Body:
                Var: c, d;
                c = 5.1;
                c = d;
            EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_assign_function_3(self):
        """Simple program: main"""
        input = """
            Function: main
            Body:
                Var: x, y;
                x = 5 + 9 * 2 - 3;
                y = 5.1 + "haha";
            EndBody.
                """
        expect = str(
            TypeMismatchInExpression(
                BinaryOp("+", FloatLiteral(5.1), StringLiteral("haha"))
            )
        )
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_function_4(self):
        """Simple program: main"""
        input = """
            Function: main
            Body:
                Var: x, y, z, t;
                x = y + z;
                t = x + 5.1;
            EndBody.
                """
        expect = str(
            TypeMismatchInExpression(BinaryOp("+", Id("x"), FloatLiteral(5.1)))
        )
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_assign_function_5(self):
        """Simple program: main"""
        input = """
            Function: main
            Body:
                Var: x, y, z, t;
                x = 1;
                y = x + 2;
                z = ((x + y) * t) >= (4 \\ (-t));
            EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_assign_function_6(self):
        """Simple program: main"""
        input = """
            Var: x, y;

            Function: main
            Parameter: x, y
            Body:
                Var: a;
                x = 1 + 2 * 3 \\ 4;
                y = True;
                Return a + x;
            EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_assign_function_7(self):
        """Simple program: main"""
        input = """
            Var: a;

            Function: foo
            Parameter: b
            Body:
                a = 2;
                Return b * 2;
            EndBody.

            Function: main
            Body:
                Return foo(1);
            EndBody.
                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_assign_function_8(self):
        """Simple program: main"""
        input = """
            Var: a;

            Function: main
            Body:
                a = foo(1) + 1;
                Return;
            EndBody.

            Function: foo
            Parameter: b
            Body:
                Return 2.5;
            EndBody.
                """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(2.5))))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_assign_function_9(self):
        """Simple program: main"""
        input = """
            Function: f
            Parameter: a
            Body:
                a = 1;
                Return;
            EndBody.

            Function: main
            Parameter: b
            Body:
                If b||(1 + 2 > 3) Then
                    f(b);
                EndIf.
            EndBody.

                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("f"), [Id("b")])))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_assign_function_9(self):
        """Simple program: main"""
        input = """
            Function: main
            Parameter: x
            Body:
                x = 1;
                Return 2.5;
            EndBody.

                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_assign_function_10(self):
        """Simple program: main"""
        input = """
            Function: main
            Parameter: x, y
            Body:
                Return foo();
            EndBody.

                """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_number_9(self):
        """if wrong second"""
        raw_input = """
            Function: main
            Parameter: a,b,c
            Body:
                If a==b Then
                    a=5;
                ElseIf 1.1 *. 2e3 Then
                    Return;
                EndIf.
            EndBody.
            """
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [
                        VarDecl(Id("a"), [], None),
                        VarDecl(Id("b"), [], None),
                        VarDecl(Id("c"), [], None),
                    ],
                    (
                        [],
                        [
                            If(
                                [
                                    [
                                        BinaryOp("==", Id("a"), Id("b")),
                                        [],
                                        [Assign(Id("a"), IntLiteral(5))],
                                    ],
                                    [
                                        BinaryOp(
                                            "*.",
                                            FloatLiteral(1.1),
                                            FloatLiteral(2000.0),
                                        ),
                                        [],
                                        [Return(None)],
                                    ],
                                ],
                                ([], []),
                            )
                        ],
                    ),
                )
            ]
        )
        expect = str(
            TypeMismatchInStatement(
                If(
                    [
                        [
                            BinaryOp("==", Id("a"), Id("b")),
                            [],
                            [Assign(Id("a"), IntLiteral(5))],
                        ],
                        [
                            BinaryOp("*.", FloatLiteral(1.1), FloatLiteral(2000.0)),
                            [],
                            [Return(None)],
                        ],
                    ],
                    ([], []),
                )
            )
        )
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_diff_numofparam_stmt(self):
        """Complex program"""
        input = """Function: main
                    Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_undeclared_function_use_ast(self):
        """Simple program: main"""
        input = Program(
            [FuncDecl(name=Id("main"), param=[], body=([], [CallStmt(Id("foo"), [])]))]
        )
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program(
            [
                FuncDecl(
                    Id("main"),
                    [],
                    (
                        [],
                        [
                            CallStmt(
                                Id("printStrLn"),
                                [CallExpr(Id("read"), [IntLiteral(4)])],
                            )
                        ],
                    ),
                )
            ]
        )
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([], [CallStmt(Id("printStrLn"), [])]))]
        )
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 419))
        self.assertTrue(TestChecker.test(input, expect, 419))
