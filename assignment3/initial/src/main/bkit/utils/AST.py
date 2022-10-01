from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from Visitor import Visitor


def printlist(lst, f=str, start="[", sepa=",", ending="]"):
    return start + sepa.join(f(i) for i in lst) + ending


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Stmt(AST):
    __metaclass__ = ABCMeta
    pass


class Decl(AST):
    __metaclass__ = ABCMeta
    pass


class Expr(AST):
    __metaclass__ = ABCMeta
    pass


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Id(LHS):
    name: str

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)


@dataclass
class Program(AST):
    decl: List[Decl]

    def __str__(self):
        return "Program(" + printlist(self.decl) + ")"

    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)


@dataclass
class VarDecl(Decl):
    variable: Id
    varDimen: List[int]  # empty list for scalar variable
    varInit: Literal  # null if no initial

    def __str__(self):
        initial = ("," + str(self.varInit)) if self.varInit else ""
        dimen = ("," + printlist(self.varDimen)) if self.varDimen else ""
        return "VarDecl(" + str(self.variable) + dimen + initial + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


@dataclass
class FuncDecl(Decl):
    name: Id
    param: List[VarDecl]
    body: Tuple[List[VarDecl], List[Stmt]]

    def __str__(self):
        return (
            "FuncDecl("
            + str(self.name)
            + printlist(self.param)
            + ",("
            + printlist(self.body[0])
            + printlist(self.body[1])
            + "))"
        )

    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


@dataclass
class ArrayCell(LHS):
    arr: Expr
    idx: List[Expr]

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + printlist(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)


@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr

    def __str__(self):
        return (
            "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"
        )

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)


@dataclass
class UnaryOp(Expr):
    op: str
    body: Expr

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)


@dataclass
class CallExpr(Expr):
    method: Id
    param: List[Expr]

    def __str__(self):
        return "CallExpr(" + str(self.method) + "," + printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)


@dataclass
class IntLiteral(Literal):
    value: int

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)


@dataclass
class FloatLiteral(Literal):
    value: float

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)


@dataclass
class StringLiteral(Literal):
    value: str

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)


@dataclass
class BooleanLiteral(Literal):
    value: bool

    def __str__(self):
        return "BooleanLiteral(" + str(self.value).lower() + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)


@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]

    def __str__(self):
        return printlist(self.value, start="ArrayLiteral(", ending=")")

    def accept(self, v, param):
        return v.visitArrayLiteral(self, param)


@dataclass
class Assign(Stmt):
    lhs: LHS
    rhs: Expr

    def __str__(self):
        return "Assign(" + str(self.lhs) + "," + str(self.rhs) + ")"

    def accept(self, v, param):
        return v.visitAssign(self, param)


def printListStmt(stmt):
    return printlist(stmt[0]) + "," + printlist(stmt[1])


def printIfThenStmt(stmt):
    return str(stmt[0]) + "," + printListStmt((stmt[1], stmt[2]))


@dataclass
class If(Stmt):
    """Expr is the condition,
    List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
    List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """

    ifthenStmt: List[Tuple[Expr, List[VarDecl], List[Stmt]]]
    elseStmt: Tuple[List[VarDecl], List[Stmt]]  # for Else branch, empty list if no Else

    def __str__(self):
        ifstmt = printlist(self.ifthenStmt, printIfThenStmt, "If(", ")ElseIf(", ")")
        elsestmt = (
            ("Else(" + printListStmt(self.elseStmt) + ")") if self.elseStmt else ""
        )
        return ifstmt + elsestmt

    def accept(self, v, param):
        return v.visitIf(self, param)


@dataclass
class For(Stmt):
    idx1: Id
    expr1: Expr
    expr2: Expr
    expr3: Expr
    loop: Tuple[List[VarDecl], List[Stmt]]

    def __str__(self):
        return (
            "For("
            + str(self.idx1)
            + ","
            + str(self.expr1)
            + ","
            + str(self.expr2)
            + ","
            + str(self.expr3)
            + ","
            + printListStmt(self.loop)
            + ")"
        )

    def accept(self, v, param):
        return v.visitFor(self, param)


class Break(Stmt):
    def __str__(self):
        return "Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)


class Continue(Stmt):
    def __str__(self):
        return "Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)


@dataclass
class Return(Stmt):
    expr: Expr  # None if no expression

    def __str__(self):
        return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)


@dataclass
class Dowhile(Stmt):
    sl: Tuple[List[VarDecl], List[Stmt]]
    exp: Expr

    def __str__(self):
        return "Dowhile(" + printListStmt(self.sl) + "," + str(self.exp) + ")"

    def accept(self, v, param):
        return v.visitDowhile(self, param)


@dataclass
class While(Stmt):
    exp: Expr
    sl: Tuple[List[VarDecl], List[Stmt]]

    def __str__(self):
        return "While(" + str(self.exp) + "," + printListStmt(self.sl) + ")"

    def accept(self, v, param):
        return v.visitWhile(self, param)


@dataclass
class CallStmt(Stmt):
    method: Id
    param: List[Expr]

    def __str__(self):
        return "CallStmt(" + str(self.method) + "," + printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallStmt(self, param)
