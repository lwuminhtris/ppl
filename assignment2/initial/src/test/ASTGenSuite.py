import unittest
from TestUtils import TestAST
from AST import *


# added
from main.bkit.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program_0(self):
        """Simple program: int main() {}"""
        input = """Var: a;"""
        expect = Program(
            decl=[VarDecl(variable=Id(name="a"), varDimen=[], varInit=None)]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_simple_program_1(self):
        """Simple program: int main() {}"""
        input = """Var: a, b;"""
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                VarDecl(variable=Id(name="b"), varDimen=[], varInit=None),
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_simple_program_2(self):
        """Simple program: int main() {}"""
        input = """Var: a, b = 2, c[1][2] = 3;"""
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                VarDecl(
                    variable=Id(name="b"), varDimen=[], varInit=IntLiteral(value=2)
                ),
                VarDecl(
                    variable=Id(name="c"), varDimen=[1, 2], varInit=IntLiteral(value=3)
                ),
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_simple_program_3(self):
        """Simple program: int main() {}"""
        input = """Var: longest_time, me = 0x12, d[0x11][4] = {1, 2};"""
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="longest_time"), varDimen=[], varInit=None),
                VarDecl(
                    variable=Id(name="me"), varDimen=[], varInit=IntLiteral(value=18)
                ),
                VarDecl(
                    variable=Id(name="d"),
                    varDimen=[17, 4],
                    varInit=ArrayLiteral(
                        value=[IntLiteral(value=1), IntLiteral(value=2)]
                    ),
                ),
            ]
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_number_4(self):
        """Function no endline"""
        input = """
            Var: a, b;
            Var: x, y = 1;
            Var: k[2], k[3] = 4;
        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                VarDecl(variable=Id(name="b"), varDimen=[], varInit=None),
                VarDecl(variable=Id(name="x"), varDimen=[], varInit=None),
                VarDecl(
                    variable=Id(name="y"), varDimen=[], varInit=IntLiteral(value=1)
                ),
                VarDecl(variable=Id(name="k"), varDimen=[2], varInit=None),
                VarDecl(
                    variable=Id(name="k"), varDimen=[3], varInit=IntLiteral(value=4)
                ),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                304,
            )
        )

    def test_number_5(self):
        """Function no endline"""
        input = """
        Var: a;

        Function: main
        Body:

        EndBody.
        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                FuncDecl(name=Id(name="main"), param=[], body=([], [])),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                305,
            )
        )

    def test_number_6(self):
        """Function no endline"""
        input = """
        Var: a;

        Function: main
        Parameter: b, c[1]
        Body:

        EndBody.
        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                FuncDecl(
                    name=Id(name="main"),
                    param=[
                        VarDecl(variable=Id(name="b"), varDimen=[], varInit=None),
                        VarDecl(variable=Id(name="c"), varDimen=[1], varInit=None),
                    ],
                    body=([], []),
                ),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                306,
            )
        )

    def test_number_7(self):
        """Function no endline"""
        input = """
        Var: a, b = 2, c[1], d[2] = {3, "Haha"};

        Function: foo1
        Parameter: f1, f2
        Body:
        EndBody.

        Function: foo2
        Body:
        EndBody.

        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                VarDecl(
                    variable=Id(name="b"), varDimen=[], varInit=IntLiteral(value=2)
                ),
                VarDecl(variable=Id(name="c"), varDimen=[1], varInit=None),
                VarDecl(
                    variable=Id(name="d"),
                    varDimen=[2],
                    varInit=ArrayLiteral(
                        value=[IntLiteral(value=3), StringLiteral(value="Haha")]
                    ),
                ),
                FuncDecl(
                    name=Id(name="foo1"),
                    param=[
                        VarDecl(variable=Id(name="f1"), varDimen=[], varInit=None),
                        VarDecl(variable=Id(name="f2"), varDimen=[], varInit=None),
                    ],
                    body=([], []),
                ),
                FuncDecl(name=Id(name="foo2"), param=[], body=([], [])),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                307,
            )
        )

    def test_number_8(self):
        """Function no endline"""
        input = """
        Function: main
        Parameter: a, b
        Body:
            Var: x, y = 2;
            If y >= 2 Then
                Return;
            EndIf.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[
                        VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                        VarDecl(variable=Id(name="b"), varDimen=[], varInit=None),
                    ],
                    body=(
                        [
                            VarDecl(variable=Id(name="x"), varDimen=[], varInit=None),
                            VarDecl(
                                variable=Id(name="y"),
                                varDimen=[],
                                varInit=IntLiteral(value=2),
                            ),
                        ],
                        [
                            If(
                                ifthenStmt=[
                                    [
                                        BinaryOp(
                                            op=">=",
                                            left=Id(name="y"),
                                            right=IntLiteral(value=2),
                                        ),
                                        [],
                                        [Return(expr=None)],
                                    ]
                                ],
                                elseStmt=([], []),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                308,
            )
        )

    def test_number_9(self):
        """Function no endline"""
        input = r"""
        Var: str="I love you \n so much";
        Function: main
        Body:
            print(str);
        EndBody.
        """
        expect = Program(
            decl=[
                VarDecl(
                    variable=Id(name="str"),
                    varDimen=[],
                    varInit=StringLiteral(value="I love you \\n so much"),
                ),
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [CallStmt(method=Id(name="print"), param=[Id(name="str")])],
                    ),
                ),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                309,
            )
        )

    def test_number_10(self):
        """Function no endline"""
        input = """
        Function: main
        Body:
            Var: x;
            For(i=1, i<0x1A, 1) Do
                x = x + 1;
            EndFor.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [VarDecl(variable=Id(name="x"), varDimen=[], varInit=None)],
                        [
                            For(
                                idx1=Id(name="i"),
                                expr1=IntLiteral(value=1),
                                expr2=BinaryOp(
                                    op="<",
                                    left=Id(name="i"),
                                    right=IntLiteral(value=26),
                                ),
                                expr3=IntLiteral(value=1),
                                loop=(
                                    [],
                                    [
                                        Assign(
                                            lhs=Id(name="x"),
                                            rhs=BinaryOp(
                                                op="+",
                                                left=Id(name="x"),
                                                right=IntLiteral(value=1),
                                            ),
                                        )
                                    ],
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                310,
            )
        )

    def test_number_11(self):
        """Function no endline"""
        input = """
        Function: a
        Parameter: x
        Body:
            Var: y;
            For(i=1, i%2!=0, (1+2)>3) Do
                Var: z;
            EndFor.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="a"),
                    param=[VarDecl(variable=Id(name="x"), varDimen=[], varInit=None)],
                    body=(
                        [VarDecl(variable=Id(name="y"), varDimen=[], varInit=None)],
                        [
                            For(
                                idx1=Id(name="i"),
                                expr1=IntLiteral(value=1),
                                expr2=BinaryOp(
                                    op="!=",
                                    left=BinaryOp(
                                        op="%",
                                        left=Id(name="i"),
                                        right=IntLiteral(value=2),
                                    ),
                                    right=IntLiteral(value=0),
                                ),
                                expr3=BinaryOp(
                                    op=">",
                                    left=BinaryOp(
                                        op="+",
                                        left=IntLiteral(value=1),
                                        right=IntLiteral(value=2),
                                    ),
                                    right=IntLiteral(value=3),
                                ),
                                loop=(
                                    [
                                        VarDecl(
                                            variable=Id(name="z"),
                                            varDimen=[],
                                            varInit=None,
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                311,
            )
        )

    def test_number_12(self):
        """Function no endline"""
        input = """
        Function: main
        Body:
            foo(1, 2)[3] = 4;
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=CallExpr(
                                        method=Id(name="foo"),
                                        param=[
                                            IntLiteral(value=1),
                                            IntLiteral(value=2),
                                        ],
                                    ),
                                    idx=[IntLiteral(value=3)],
                                ),
                                rhs=IntLiteral(value=4),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                312,
            )
        )

    def test_number_13(self):
        """Function no endline"""
        input = """
        Function: main
        Body:
            If a Then
                Return;
            ElseIf b Then
                Continue;
            Else
                Return;
            EndIf.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [
                            If(
                                ifthenStmt=[
                                    [Id(name="a"), [], [Return(expr=None)]],
                                    [Id(name="b"), [], [Continue()]],
                                ],
                                elseStmt=([], [Return(expr=None)]),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                313,
            )
        )

    def test_number_14(self):
        """Function no endline"""
        input = """
        Function: main
        Body:
            smt_12(1,2,a[2][-False])[0x12+6] = haha[1][!!3];
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=CallExpr(
                                        method=Id(name="smt_12"),
                                        param=[
                                            IntLiteral(value=1),
                                            IntLiteral(value=2),
                                            ArrayCell(
                                                arr=Id(name="a"),
                                                idx=[
                                                    IntLiteral(value=2),
                                                    UnaryOp(
                                                        op="-",
                                                        body=BooleanLiteral(
                                                            value=False
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    idx=[
                                        BinaryOp(
                                            op="+",
                                            left=IntLiteral(value=18),
                                            right=IntLiteral(value=6),
                                        )
                                    ],
                                ),
                                rhs=ArrayCell(
                                    arr=Id(name="haha"),
                                    idx=[
                                        IntLiteral(value=1),
                                        UnaryOp(
                                            op="!",
                                            body=UnaryOp(
                                                op="!", body=IntLiteral(value=3)
                                            ),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                314,
            )
        )

    def test_number_15(self):
        """Function no endline"""
        input = """
        Function: main
        Body:
            Do x = x + 1; While
                1+(2*3-True)*.False < -(!2)
            EndDo.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [
                            Dowhile(
                                sl=(
                                    [],
                                    [
                                        Assign(
                                            lhs=Id(name="x"),
                                            rhs=BinaryOp(
                                                op="+",
                                                left=Id(name="x"),
                                                right=IntLiteral(value=1),
                                            ),
                                        )
                                    ],
                                ),
                                exp=BinaryOp(
                                    op="<",
                                    left=BinaryOp(
                                        op="+",
                                        left=IntLiteral(value=1),
                                        right=BinaryOp(
                                            op="*.",
                                            left=BinaryOp(
                                                op="-",
                                                left=BinaryOp(
                                                    op="*",
                                                    left=IntLiteral(value=2),
                                                    right=IntLiteral(value=3),
                                                ),
                                                right=BooleanLiteral(value=True),
                                            ),
                                            right=BooleanLiteral(value=False),
                                        ),
                                    ),
                                    right=UnaryOp(
                                        op="-",
                                        body=UnaryOp(op="!", body=IntLiteral(value=2)),
                                    ),
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                315,
            )
        )

    def test_number_16(self):
        """Special test case for ArrayCell with Expr"""
        input = """
        Function: main
        Parameter: a,  b[1]
        Body:
            (foo() + 2)[2][3] = 1*True+(2*3)-.4;
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[
                        VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                        VarDecl(variable=Id(name="b"), varDimen=[1], varInit=None),
                    ],
                    body=(
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=BinaryOp(
                                        op="+",
                                        left=CallExpr(method=Id(name="foo"), param=[]),
                                        right=IntLiteral(value=2),
                                    ),
                                    idx=[IntLiteral(value=2), IntLiteral(value=3)],
                                ),
                                rhs=BinaryOp(
                                    op="-.",
                                    left=BinaryOp(
                                        op="+",
                                        left=BinaryOp(
                                            op="*",
                                            left=IntLiteral(value=1),
                                            right=BooleanLiteral(value=True),
                                        ),
                                        right=BinaryOp(
                                            op="*",
                                            left=IntLiteral(value=2),
                                            right=IntLiteral(value=3),
                                        ),
                                    ),
                                    right=IntLiteral(value=4),
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                316,
            )
        )

    def test_number_17(self):
        """Array Cell testing"""
        input = """
        Function: main
        Body:
            Var: a;
            foo()[x()][y()] = 0.4;
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [VarDecl(variable=Id(name="a"), varDimen=[], varInit=None)],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=CallExpr(method=Id(name="foo"), param=[]),
                                    idx=[
                                        CallExpr(method=Id(name="x"), param=[]),
                                        CallExpr(method=Id(name="y"), param=[]),
                                    ],
                                ),
                                rhs=FloatLiteral(value=0.4),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                317,
            )
        )

    def test_number_18(self):
        """Function no endline"""
        input = """
        Function: convert_to_int
        Body:
            Var: a;
            If a Then
                a = array[1][2];
            EndIf.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="convert_to_int"),
                    param=[],
                    body=(
                        [VarDecl(variable=Id(name="a"), varDimen=[], varInit=None)],
                        [
                            If(
                                ifthenStmt=[
                                    [
                                        Id(name="a"),
                                        [],
                                        [
                                            Assign(
                                                lhs=Id(name="a"),
                                                rhs=ArrayCell(
                                                    arr=Id(name="array"),
                                                    idx=[
                                                        IntLiteral(value=1),
                                                        IntLiteral(value=2),
                                                    ],
                                                ),
                                            )
                                        ],
                                    ]
                                ],
                                elseStmt=([], []),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                318,
            )
        )

    def test_number_19(self):
        """Function no endline"""
        input = r"""
        Function: main
        Body:
            a[1][2] = {{1, 0o12}, {"haha", 1.e+7}, True};
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [],
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=Id(name="a"),
                                    idx=[IntLiteral(value=1), IntLiteral(value=2)],
                                ),
                                rhs=ArrayLiteral(
                                    value=[
                                        ArrayLiteral(
                                            value=[
                                                IntLiteral(value=1),
                                                IntLiteral(value=10),
                                            ]
                                        ),
                                        ArrayLiteral(
                                            value=[
                                                StringLiteral(value="haha"),
                                                FloatLiteral(value=10000000.0),
                                            ]
                                        ),
                                        BooleanLiteral(value=True),
                                    ]
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                319,
            )
        )

    def test_number_20(self):
        """Function no endline"""
        input = r"""
        Function: main
        Body:

        EndBody.
        """
        expect = Program(decl=[FuncDecl(name=Id(name="main"), param=[], body=([], []))])
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                320,
            )
        )

    def test_number_21(self):
        """Function no endline"""
        input = r"""
        Function: fib
        Parameter: a
        Body:
            If a == 1 Then
                Return 1;
            Else
                Return a * fib(a - 1);
            EndIf.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="fib"),
                    param=[VarDecl(variable=Id(name="a"), varDimen=[], varInit=None)],
                    body=(
                        [],
                        [
                            If(
                                ifthenStmt=[
                                    [
                                        BinaryOp(
                                            op="==",
                                            left=Id(name="a"),
                                            right=IntLiteral(value=1),
                                        ),
                                        [],
                                        [Return(expr=IntLiteral(value=1))],
                                    ]
                                ],
                                elseStmt=(
                                    [],
                                    [
                                        Return(
                                            expr=BinaryOp(
                                                op="*",
                                                left=Id(name="a"),
                                                right=CallExpr(
                                                    method=Id(name="fib"),
                                                    param=[
                                                        BinaryOp(
                                                            op="-",
                                                            left=Id(name="a"),
                                                            right=IntLiteral(value=1),
                                                        )
                                                    ],
                                                ),
                                            )
                                        )
                                    ],
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                321,
            )
        )

    def test_number_22(self):
        """Function no endline"""
        input = r"""

        """
        expect = Program([])
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                322,
            )
        )

    def test_number_23(self):
        """Function no endline"""
        input = r"""
        Var: a, b = 2, c[1] = 3;
        Var: d="so fvcking \t funny";

        Function: main
        Parameter: a, b[1]
        Body:
            Var: x;
            Do
                Var: y;
            While x > a EndDo.
        EndBody.

        Function: util
        Body:
            Break;
        EndBody.
        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                VarDecl(
                    variable=Id(name="b"), varDimen=[], varInit=IntLiteral(value=2)
                ),
                VarDecl(
                    variable=Id(name="c"), varDimen=[1], varInit=IntLiteral(value=3)
                ),
                VarDecl(
                    variable=Id(name="d"),
                    varDimen=[],
                    varInit=StringLiteral(value="so fvcking \\t funny"),
                ),
                FuncDecl(
                    name=Id(name="main"),
                    param=[
                        VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                        VarDecl(variable=Id(name="b"), varDimen=[1], varInit=None),
                    ],
                    body=(
                        [VarDecl(variable=Id(name="x"), varDimen=[], varInit=None)],
                        [
                            Dowhile(
                                sl=(
                                    [
                                        VarDecl(
                                            variable=Id(name="y"),
                                            varDimen=[],
                                            varInit=None,
                                        )
                                    ],
                                    [],
                                ),
                                exp=BinaryOp(
                                    op=">", left=Id(name="x"), right=Id(name="a")
                                ),
                            )
                        ],
                    ),
                ),
                FuncDecl(name=Id(name="util"), param=[], body=([], [Break()])),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                323,
            )
        )

    def test_number_24(self):
        """Function no endline"""
        input = r"""
        Var: a;

        Function: test
        Parameter: b
        Body:
            Var: c;
            While b < 0x12 Do
                Var: d;
                Return d + c;
            EndWhile.
        EndBody.
        """
        expect = Program(
            decl=[
                VarDecl(variable=Id(name="a"), varDimen=[], varInit=None),
                FuncDecl(
                    name=Id(name="test"),
                    param=[VarDecl(variable=Id(name="b"), varDimen=[], varInit=None)],
                    body=(
                        [VarDecl(variable=Id(name="c"), varDimen=[], varInit=None)],
                        [
                            While(
                                exp=BinaryOp(
                                    op="<",
                                    left=Id(name="b"),
                                    right=IntLiteral(value=18),
                                ),
                                sl=(
                                    [
                                        VarDecl(
                                            variable=Id(name="d"),
                                            varDimen=[],
                                            varInit=None,
                                        )
                                    ],
                                    [
                                        Return(
                                            expr=BinaryOp(
                                                op="+",
                                                left=Id(name="d"),
                                                right=Id(name="c"),
                                            )
                                        )
                                    ],
                                ),
                            )
                        ],
                    ),
                ),
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                324,
            )
        )

    def test_number_25(self):
        """Function no endline"""
        input = r"""
        Function: main
        Body:
            Var: a;
            For(i=1, i\.2>=2.e-7, !False) Do
                Var: b[1][2] = 3;
                While i < False Do
                    Var: c;
                    c = c + 2.4e-5 * foo(3)[1];
                    Do
                        Var: d;
                        i = i + 1;
                        If i == j Then
                            Var: e;
                            Return e;
                        EndIf.
                    While i > True + 0o12 EndDo.
                EndWhile.
            EndFor.
        EndBody.
        """
        expect = Program(
            decl=[
                FuncDecl(
                    name=Id(name="main"),
                    param=[],
                    body=(
                        [VarDecl(variable=Id(name="a"), varDimen=[], varInit=None)],
                        [
                            For(
                                idx1=Id(name="i"),
                                expr1=IntLiteral(value=1),
                                expr2=BinaryOp(
                                    op=">=",
                                    left=BinaryOp(
                                        op="\\.",
                                        left=Id(name="i"),
                                        right=IntLiteral(value=2),
                                    ),
                                    right=FloatLiteral(value=2e-07),
                                ),
                                expr3=UnaryOp(op="!", body=BooleanLiteral(value=False)),
                                loop=(
                                    [
                                        VarDecl(
                                            variable=Id(name="b"),
                                            varDimen=[1, 2],
                                            varInit=IntLiteral(value=3),
                                        )
                                    ],
                                    [
                                        While(
                                            exp=BinaryOp(
                                                op="<",
                                                left=Id(name="i"),
                                                right=BooleanLiteral(value=False),
                                            ),
                                            sl=(
                                                [
                                                    VarDecl(
                                                        variable=Id(name="c"),
                                                        varDimen=[],
                                                        varInit=None,
                                                    )
                                                ],
                                                [
                                                    Assign(
                                                        lhs=Id(name="c"),
                                                        rhs=BinaryOp(
                                                            op="+",
                                                            left=Id(name="c"),
                                                            right=BinaryOp(
                                                                op="*",
                                                                left=FloatLiteral(
                                                                    value=2.4e-05
                                                                ),
                                                                right=ArrayCell(
                                                                    arr=CallExpr(
                                                                        method=Id(
                                                                            name="foo"
                                                                        ),
                                                                        param=[
                                                                            IntLiteral(
                                                                                value=3
                                                                            )
                                                                        ],
                                                                    ),
                                                                    idx=[
                                                                        IntLiteral(
                                                                            value=1
                                                                        )
                                                                    ],
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                    Dowhile(
                                                        sl=(
                                                            [
                                                                VarDecl(
                                                                    variable=Id(
                                                                        name="d"
                                                                    ),
                                                                    varDimen=[],
                                                                    varInit=None,
                                                                )
                                                            ],
                                                            [
                                                                Assign(
                                                                    lhs=Id(name="i"),
                                                                    rhs=BinaryOp(
                                                                        op="+",
                                                                        left=Id(
                                                                            name="i"
                                                                        ),
                                                                        right=IntLiteral(
                                                                            value=1
                                                                        ),
                                                                    ),
                                                                ),
                                                                If(
                                                                    ifthenStmt=[
                                                                        [
                                                                            BinaryOp(
                                                                                op="==",
                                                                                left=Id(
                                                                                    name="i"
                                                                                ),
                                                                                right=Id(
                                                                                    name="j"
                                                                                ),
                                                                            ),
                                                                            [
                                                                                VarDecl(
                                                                                    variable=Id(
                                                                                        name="e"
                                                                                    ),
                                                                                    varDimen=[],
                                                                                    varInit=None,
                                                                                )
                                                                            ],
                                                                            [
                                                                                Return(
                                                                                    expr=Id(
                                                                                        name="e"
                                                                                    )
                                                                                )
                                                                            ],
                                                                        ]
                                                                    ],
                                                                    elseStmt=([], []),
                                                                ),
                                                            ],
                                                        ),
                                                        exp=BinaryOp(
                                                            op=">",
                                                            left=Id(name="i"),
                                                            right=BinaryOp(
                                                                op="+",
                                                                left=BooleanLiteral(
                                                                    value=True
                                                                ),
                                                                right=IntLiteral(
                                                                    value=10
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        )
                                    ],
                                ),
                            )
                        ],
                    ),
                )
            ]
        )
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                325,
            )
        )

    def test_number_26(self):
        """Function no endline"""
        input = r"""

        """
        expect = Program([])
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                326,
            )
        )

    def test_number_27(self):
        """Function no endline"""
        input = r"""

        """
        expect = Program([])
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                327,
            )
        )

    def test_number_28(self):
        """Function no endline"""
        input = r"""

        """
        expect = Program([])
        self.assertTrue(
            TestAST.checkASTGen(
                input,
                expect,
                328,
            )
        )

