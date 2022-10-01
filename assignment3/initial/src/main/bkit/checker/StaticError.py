# update: 6/11/2020
from abc import ABC
from dataclasses import dataclass
from AST import *


class Kind(ABC):
    pass


class Function(Kind):
    def __str__(self):
        return "Function"


class Parameter(Kind):
    def __str__(self):
        return "Parameter"


class Variable(Kind):
    def __str__(self):
        return "Variable"


class Identifier(Kind):
    def __str__(self):
        return "Identifier"


class StaticError(Exception):
    pass


@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self):
        return "Undeclared " + str(self.k) + ": " + self.n


@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str  # name of identifier

    def __str__(self):
        return "Redeclared " + str(self.k) + ": " + self.n


@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        return "Type Mismatch In Expression: " + str(self.exp)


@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Mismatch In Statement: " + str(self.stmt)


@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Cannot Be Inferred: " + str(self.stmt)


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"


@dataclass
class NotInLoop(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Statement Not In Loop: " + str(self.stmt)


@dataclass
class InvalidArrayLiteral(StaticError):
    arr: ArrayLiteral

    def __str__(self):
        return "Invalid Array Literal: " + str(self.arr)


@dataclass
class FunctionNotReturn(StaticError):
    name: str

    def __str__(self):
        return "Function Not Return: " + self.name


@dataclass
class UnreachableFunction(StaticError):
    name: str

    def __str__(self):
        return "Unreachable Function: " + self.name


@dataclass
class UnreachableStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Unreachable Statement: " + str(self.stmt)


@dataclass
class IndexOutOfRange(StaticError):
    cell: ArrayCell

    def __str__(self):
        return "Index Out Of Range: " + str(self.cell)
