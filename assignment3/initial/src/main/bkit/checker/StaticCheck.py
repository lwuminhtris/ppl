"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class IntType(Prim):
    def __init__(self):
        return

    def __repr__(self):
        return "IntType"


class FloatType(Prim):
    def __init__(self):
        return

    def __repr__(self):
        return "FloatType"


class StringType(Prim):
    def __init__(self):
        return

    def __repr__(self):
        return "StringType"


class BoolType(Prim):
    def __init__(self):
        return

    def __repr__(self):
        return "BoolType"


class VoidType(Type):
    def __init__(self):
        return

    def __repr__(self):
        return "VoidType"


class Unknown(Type):
    def __init__(self):
        return

    def __repr__(self):
        return "Unknown"


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        if self.dimen == other.dimen:
            if self.eletype.value == other.eletype.value:
                return True
            if isinstance(self.eletype.value, Unknown) and not isinstance(
                other.eletype.value, Unknown
            ):
                self.eletype.value = other.eletype.value
                return True
            if isinstance(other.eletype.value, Unknown) and not isinstance(
                self.eletype.value, Unknown
            ):
                other.eletype.value = self.eletype.value
                return True
        return False


@dataclass
class Symbol:
    name: str
    mtype: Type
    paramTypes: List[Type] = None
    returnType: Type = None

    def __repr__(self) -> str:
        return (
            "Symbol("
            + str(self.name)
            + ", "
            + str(self.mtype)
            + str(self.params_to_str())
            + str(self.return_to_str())
            + ")"
        )

    def params_to_str(self):
        if self.paramTypes:
            s = ""
            for param in self.paramTypes.value:
                s = (
                    s + ", " + str(param.mtype)
                    if param != self.paramTypes.value[0]
                    else s + str(param.mtype)
                )
            return ", Params([" + s + "])"
        else:
            return ""

    def return_to_str(self):
        if self.returnType:
            return ", ReturnType(" + str(self.returnType) + ")"
        else:
            return ""


class Wrapper:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return "Wrapper(" + str(self.value) + ")"


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol(
                "int_of_float",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(FloatType()))]),
                Wrapper(IntType()),
            ),
            Symbol(
                "float_to_int",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(IntType()))]),
                Wrapper(FloatType()),
            ),
            Symbol(
                "int_of_string",
                Wrapper(Function()),
                Wrapper([Symbol(None, StringType())]),
                Wrapper(IntType()),
            ),
            Symbol(
                "string_of_int",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(IntType()))]),
                Wrapper(StringType()),
            ),
            Symbol(
                "float_of_string",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(StringType()))]),
                Wrapper(FloatType()),
            ),
            Symbol(
                "string_of_float",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(FloatType()))]),
                Wrapper(StringType()),
            ),
            Symbol(
                "bool_of_string",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(StringType()))]),
                Wrapper(BoolType()),
            ),
            Symbol(
                "string_of_bool",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(BoolType()))]),
                Wrapper(StringType()),
            ),
            Symbol("read", Wrapper(Function()), Wrapper([]), Wrapper(StringType())),
            Symbol("printLn", Wrapper(Function()), Wrapper([]), Wrapper(VoidType())),
            Symbol(
                "printStr",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(StringType()))]),
                Wrapper(VoidType()),
            ),
            Symbol(
                "printStrLn",
                Wrapper(Function()),
                Wrapper([Symbol(None, Wrapper(StringType()))]),
                Wrapper(VoidType()),
            ),
        ]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitId(self, ast, env):
        return ast.name

    def checkNoEntryPoint(self, env):
        for symbol in env:
            if isinstance(symbol, Symbol) and isinstance(symbol.mtype.value, Function):
                if symbol.name == "main":
                    return
        raise NoEntryPoint()

    def visitProgram(self, ast, env):
        # IMPORTANT: env = [] is for debug only
        # env = []
        # ->
        """
        First, visit all the global vardecls and functions to get their initialization
        """
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                env = [self.createVarDecl(decl, env)] + env
            if isinstance(decl, FuncDecl):
                env = [self.createFuncDecl(decl, env)] + env

        self.checkNoEntryPoint(env)

        """
        In this step, we have already checked redeclaration for global scope
        After get all the global vardecls and functions we will continue to the real assertion
        This second run contains type inference and error checking
        """

        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.visit(decl, env)

        print("Global Env:\n", env)

    def checkRedeclaredVariable(self, variable, env):
        for symbol in env:
            if isinstance(symbol, Symbol) and variable.name == symbol.name:
                print("env is", env)
                raise Redeclared(Variable(), symbol.name)

    def checkRedeclaredFunction(self, function, env):
        for symbol in env:
            if isinstance(symbol, Symbol) and function.name == symbol.name:
                raise Redeclared(Function(), symbol.name)

    def checkRedeclaredParameter(self, param, env):
        for symbol in env:
            if isinstance(symbol, Symbol) and param.name == symbol.name:
                raise Redeclared(Parameter(), symbol.name)

    def createVarDecl(self, ast, env):
        variable = self.visit(ast.variable, env)
        varDimen = ast.varDimen

        if ast.varDimen and not ast.varInit:
            varType = Wrapper(Unknown())
            for dimen in varDimen[::-1]:
                prevDimen = (
                    varType.value.dimen if type(varType.value) is ArrayType else []
                )
                varType = Wrapper(ArrayType([dimen] + prevDimen, varType))

            vardecl = Symbol(name=variable, mtype=varType)

            self.checkRedeclaredVariable(vardecl, env)

            return vardecl

        varInit = self.visit(ast.varInit, env) if ast.varInit else Wrapper(Unknown())

        vardecl = Symbol(name=variable, mtype=varInit)

        self.checkRedeclaredVariable(vardecl, env)

        return vardecl

    def visitVarDecl(self, ast, env):
        variable = self.visit(ast.variable, env)
        varDimen = ast.varDimen

        if ast.varDimen and not ast.varInit:
            varType = Wrapper(Unknown())
            for dimen in varDimen[::-1]:
                prevDimen = (
                    varType.value.dimen if type(varType.value) is ArrayType else []
                )
                varType = Wrapper(ArrayType([dimen] + prevDimen, varType))

            vardecl = Symbol(name=variable, mtype=varType)

            self.checkRedeclaredVariable(vardecl, env)

            return vardecl

        varInit = self.visit(ast.varInit, env) if ast.varInit else Wrapper(Unknown())

        vardecl = Symbol(name=variable, mtype=varInit)

        self.checkRedeclaredVariable(vardecl, env)

        return vardecl

    def createParameter(self, ast, env):
        variable = self.visit(ast.variable, env)
        varDimen = ast.varDimen

        if ast.varDimen and not ast.varInit:
            varType = Wrapper(Unknown())
            for dimen in varDimen[::-1]:
                prevDimen = (
                    varType.value.dimen if type(varType.value) is ArrayType else []
                )
                varType = Wrapper(ArrayType([dimen] + prevDimen, varType))

            vardecl = Symbol(name=variable, mtype=varType)

            self.checkRedeclaredParameter(vardecl, env)

            return vardecl

        varInit = self.visit(ast.varInit, env) if ast.varInit else Wrapper(Unknown())

        vardecl = Symbol(name=variable, mtype=varInit)

        self.checkRedeclaredParameter(vardecl, env)

        return vardecl

    def createFuncDecl(self, ast, env):

        name = self.visit(ast.name, env)

        """
        Visit Parameters
        """
        parameters = []
        for x in ast.param:
            # parameters = [self.createParameter(x, parameters)] + parameters
            parameters = [self.createParameter(x, parameters)] + parameters
        # parameters = [self.createParameter(x, parameters) for x in ast.param] + parameters

        funcdecl = Symbol(
            name=name,
            mtype=Wrapper(Function()),
            paramTypes=Wrapper(parameters),
            returnType=Wrapper(Unknown()),
        )

        self.checkRedeclaredFunction(funcdecl, env)

        return funcdecl

    def visitFuncDecl(self, ast, env):
        name = self.visit(ast.name, env)

        """
        Visit Parameters
        """
        parameters = []
        for x in ast.param:
            # parameters = [self.visit(x, parameters)] + parameters
            parameters = [self.visit(x, parameters)] + parameters

        """
        Visit VarDecls
        """
        parameters_with_vardecls = parameters
        for x in ast.body[0]:
            parameters_with_vardecls = [
                self.visit(x, parameters_with_vardecls)
            ] + parameters_with_vardecls
        # parameters_with_vardecls = [
        #     self.visit(x, parameters_with_vardecls) for x in ast.body[0]
        # ] + parameters_with_vardecls

        """
        Bring current function to the head of the env list
        """
        for element in env:
            if (
                isinstance(element, Symbol)
                and element.name == name
                and isinstance(element.mtype.value, Function)
            ):
                env.insert(0, env.pop(env.index(element)))
                break

        """
        Visit Statements
        """
        stmts = parameters_with_vardecls + env
        [self.visit(x, stmts) for x in ast.body[1]]

    def visitArrayCell(self, ast, env):
        arrayId = self.visit(ast.arr, env)
        arraySymbol = self.findIdInEnv(arrayId, env)
        arraySymbolType = arraySymbol.mtype

        if isinstance(arraySymbolType.value, Unknown) and isinstance(ast.arr, CallExpr):
            raise TypeCannotBeInferred(ast)

        if not isinstance(arraySymbolType.value, ArrayType):
            raise TypeMismatchInExpression(ast)

        if len(arraySymbolType.value.dimen) is not len(ast.idx):
            raise TypeMismatchInExpression(ast)

        for ind in ast.idx:
            indType = self.visit(ind, env)
            if type(indType) is str:
                raise TypeMismatchInExpression(ast)
            if type(indType.value) is not IntType:
                raise TypeMismatchInExpression(ast)

        while isinstance(arraySymbolType.value, ArrayType):
            arraySymbolType.value = arraySymbolType.value.eletype.value

        return arraySymbolType

        if isinstance(arraySymbol.mtype.value, Unknown):
            pass

    def visitBinaryOp(self, ast, env):
        op = ast.op

        left = self.visit(ast.left, env)
        leftType = left

        right = self.visit(ast.right, env)
        rightType = right

        if type(ast.left) == Id:
            left = self.findIdInEnv(left, env)
            leftType = left.mtype

        if type(ast.right) is Id:
            right = self.findIdInEnv(right, env)
            rightType = right.mtype

        if op in ["&&", "||"]:
            if isinstance(leftType.value, Unknown):
                leftType.value = BoolType()
            if isinstance(rightType.value, Unknown):
                rightType.value = BoolType()
            if type(leftType.value) is BoolType and type(rightType.value) is BoolType:
                if type(ast.left) is Id:
                    if self.checkIfIdIsParam(left.name, env):
                        self.paramsTypeInference(left, env)
                if type(ast.right) is Id:
                    if self.checkIfIdIsParam(right.name, env):
                        self.paramsTypeInference(right, env)
                return Wrapper(BoolType())
            if not isinstance(leftType.value, BoolType) or not isinstance(
                rightType.value, BoolType
            ):
                raise TypeMismatchInExpression(ast)

        if op in ["+", "-", "*", "\\", "%"]:
            if isinstance(leftType.value, Unknown):
                leftType.value = IntType()
            if isinstance(rightType.value, Unknown):
                rightType.value = IntType()
            if type(leftType.value) is IntType and type(rightType.value) is IntType:
                if type(ast.left) is Id:
                    if self.checkIfIdIsParam(left.name, env):
                        self.paramsTypeInference(left, env)
                if type(ast.right) is Id:
                    if self.checkIfIdIsParam(right.name, env):
                        self.paramsTypeInference(right, env)
                return Wrapper(IntType())
            if not isinstance(leftType.value, IntType) or not isinstance(
                rightType.value, IntType
            ):
                raise TypeMismatchInExpression(ast)

        if op in ["==", "!=", "<", ">", "<=", ">="]:
            if isinstance(leftType.value, Unknown):
                leftType.value = IntType()
            if isinstance(rightType.value, Unknown):
                rightType.value = IntType()
            if type(leftType.value) is IntType and type(rightType.value) is IntType:
                if type(ast.left) is Id:
                    if self.checkIfIdIsParam(left.name, env):
                        self.paramsTypeInference(left, env)
                if type(ast.right) is Id:
                    if self.checkIfIdIsParam(right.name, env):
                        self.paramsTypeInference(right, env)
                return Wrapper(BoolType())
            if not isinstance(leftType.value, IntType) or not isinstance(
                rightType.value, IntType
            ):
                raise TypeMismatchInExpression(ast)

        if op in ["+.", "-.", "*.", "\\."]:
            if isinstance(leftType.value, Unknown):
                leftType.value = FloatType()
            if isinstance(rightType.value, Unknown):
                rightType.value = FloatType()
            if type(leftType.value) is FloatType and type(rightType.value) is FloatType:
                if type(ast.left) is Id:
                    if self.checkIfIdIsParam(left.name, env):
                        self.paramsTypeInference(left, env)
                if type(ast.right) is Id:
                    if self.checkIfIdIsParam(right.name, env):
                        self.paramsTypeInference(right, env)
                return Wrapper(FloatType())
            if not isinstance(leftType.value, FloatType) or not isinstance(
                rightType.value, FloatType
            ):
                raise TypeMismatchInExpression(ast)

        if op in ["=/=", "<.", ">.", "<=.", ">=."]:
            if isinstance(leftType.value, Unknown):
                leftType.value = FloatType()
            if isinstance(rightType.value, Unknown):
                rightType.value = FloatType()
            if type(leftType.value) is FloatType and type(rightType.value) is FloatType:
                if type(ast.left) is Id:
                    if self.checkIfIdIsParam(left.name, env):
                        self.paramsTypeInference(left, env)
                if type(ast.right) is Id:
                    if self.checkIfIdIsParam(right.name, env):
                        self.paramsTypeInference(right, env)
                return Wrapper(BoolType())
            if not isinstance(leftType.value, FloatType) or not isinstance(
                rightType.value, FloatType
            ):
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, env):
        op = ast.op

        body = self.visit(ast.body, env)
        bodyType = body

        if type(ast.body) is Id:
            body = self.findIdInEnv(body, env)
            bodyType = body.mtype

        if op == "!":
            if isinstance(bodyType.value, Unknown):
                bodyType.value = BoolType()
            if isinstance(bodyType.value, BoolType):
                if type(ast.body) is Id:
                    if self.checkIfIdIsParam(body.name, env):
                        self.paramsTypeInference(body, env)
                return Wrapper(BoolType())
            if not isinstance(body.value, BoolType):
                raise TypeMismatchInExpression(ast)

        if op == "-":
            if isinstance(bodyType.value, Unknown):
                bodyType.value = IntType()
            if isinstance(bodyType.value, IntType):
                if type(ast.body) is Id:
                    if self.checkIfIdIsParam(body.name, env):
                        self.paramsTypeInference(body, env)
                return Wrapper(IntType())
            if not isinstance(body.value, IntType):
                raise TypeMismatchInExpression(ast)

        if op == "-.":
            if isinstance(bodyType.value, Unknown):
                bodyType.value = FloatType()
            if isinstance(bodyType.value, FloatType):
                if type(ast.body) is Id:
                    if self.checkIfIdIsParam(body.name, env):
                        self.paramsTypeInference(body, env)
                return Wrapper(FloatType())
            if not isinstance(body.value, FloatType):
                raise TypeMismatchInExpression(ast)

    def findFunctionInEnv(self, function, env):
        for symbol in env:
            if symbol.name == function and isinstance(symbol.mtype.value, Function):
                return symbol
        raise Undeclared(Function(), function)

    def visitCallExpr(self, ast, env):
        method = self.visit(ast.method, env)
        method = self.findFunctionInEnv(method, env)

        envParams = method.paramTypes.value
        callParamsNotFull = [self.visit(x, env) for x in ast.param]

        callParams = []
        for param in callParamsNotFull:
            if type(param) == str:
                callParams = [self.findIdInEnv(param, env).mtype] + callParams
            else:
                callParams = [param] + callParams

        if len(envParams) is not len(callParams):
            raise TypeMismatchInExpression(ast)
        else:
            for index in range(0, len(envParams)):
                if isinstance(callParams[index].value, Unknown) and isinstance(
                    envParams[index].mtype.value, Unknown
                ):
                    raise TypeCannotBeInferred(ast)
                print(envParams[index])
                if isinstance(envParams[index].mtype.value, Unknown):
                    envParams[index].mtype.value = callParams[index].value
                if isinstance(callParams[index].value, Unknown):
                    callParams[index].value = envParams[index].mtype.value
                if type(envParams[index].mtype.value) is type(callParams[index].value):
                    continue
                if type(envParams[index].mtype.value) is not type(
                    callParams[index].value
                ):
                    raise TypeMismatchInExpression(ast)

        if isinstance(method.returnType.value, VoidType):
            raise TypeMismatchInExpression(ast)

        return method.returnType

    def visitIntLiteral(self, ast, env):
        return Wrapper(IntType())

    def visitFloatLiteral(self, ast, env):
        return Wrapper(FloatType())

    def visitStringLiteral(self, ast, env):
        return Wrapper(StringType())

    def visitBooleanLiteral(self, ast, env):
        return Wrapper(BoolType())

    def visitArrayLiteral(self, ast, env):
        elems = ast.value
        elemsType = self.visit(elems[0], env)

        dimen = [len(elems)] + (
            elemsType.value.dimen if type(elemsType.value) is ArrayType else []
        )
        return Wrapper(ArrayType(dimen, elemsType))

    def paramsTypeInference(self, param, env):
        for symbol in env:
            if isinstance(symbol.mtype.value, Function):
                for function_param in symbol.paramTypes.value:
                    if param.name == function_param.name:
                        function_param.mtype.value = param.mtype.value
                        break

    def findIdInEnv(self, ids, env):
        for symbol in env:
            if symbol.name == ids:
                return symbol

        raise Undeclared(Identifier(), ids)

    def visitAssign(self, ast, env):
        left = self.visit(ast.lhs, env)
        leftType = left

        right = self.visit(ast.rhs, env)
        rightType = right

        if type(ast.lhs) == Id:
            left = self.findIdInEnv(left, env)
            leftType = left.mtype

        if type(ast.rhs) == Id:
            right = self.findIdInEnv(right, env)
            rightType = right.mtype

        """
        Type Inference
        """
        if isinstance(leftType.value, Unknown) and isinstance(rightType.value, Unknown):
            raise TypeCannotBeInferred(ast)
        if isinstance(leftType.value, Unknown):
            leftType.value = rightType.value
        if isinstance(rightType.value, Unknown):
            rightType.value = leftType.value
        if type(leftType.value) is type(rightType.value):
            # It's here that we check for ArrayType dimension
            if isinstance(leftType.value, ArrayType) and isinstance(
                rightType.value, ArrayType
            ):
                if leftType.value != rightType.value:
                    raise TypeMismatchInStatement(ast)
                else:
                    pass
        if type(leftType.value) is not type(rightType.value):
            raise TypeMismatchInStatement(ast)

        """
        Function Parameters Type Inference
        """
        if type(left) is Symbol:
            if self.checkIfIdIsParam(left.name, env):
                self.paramsTypeInference(left, env)
        if type(right) is Symbol:
            if self.checkIfIdIsParam(right.name, env):
                self.paramsTypeInference(right, env)

    def visitIf(self, ast, env):
        for ifs in ast.ifthenStmt:
            conditionalExpr = self.visit(ifs[0], env)

            if isinstance(ifs[0], Id):
                ifs[0] = self.findIdInEnv(self.visit(ifs[0], env), env)
                conditionalExpr = ifs[0].mtype

                if isinstance(conditionalExpr.value, Unknown):
                    conditionalExpr.value = BoolType()

                if not isinstance(conditionalExpr.value, Unknown):
                    if not isinstance(conditionalExpr.value, BoolType):
                        raise TypeMismatchInStatement(ast)

            if type(conditionalExpr.value) is not BoolType:
                raise TypeMismatchInStatement(ast)

            new_env = []
            new_env = [self.visit(x, new_env) for x in ifs[1]] + new_env
            [self.visit(x, new_env + env) for x in ifs[2]]

        new_env = []
        new_env = [self.visit(x, new_env) for x in ast.elseStmt[0]] + new_env
        [self.visit(x, new_env + env) for x in ast.elseStmt[1]]

    def checkIfIdIsParam(self, ids, env):
        occurs = 0
        for symbol in env:
            if symbol.name == ids:
                occurs += 1

        if occurs == 1:
            return True
        if occurs > 1:
            return False

    def visitFor(self, ast, env):
        idx = self.visit(ast.idx1, env)
        idx1 = self.findIdInEnv(idx, env)

        expr1 = self.visit(ast.expr1, env).value
        if type(expr1) is IntType:
            if isinstance(idx1.mtype.value, Unknown):
                idx1.mtype.value = expr1
            if not isinstance(idx1.mtype.value, IntType):
                raise TypeMismatchInStatement(ast)

            if self.checkIfIdIsParam(idx, env):
                self.paramsTypeInference(idx1, env)
        else:
            raise TypeMismatchInStatement(ast)

        expr2 = self.visit(ast.expr2, env).value
        if type(expr2) is not BoolType:
            raise TypeMismatchInStatement(ast)

        expr3 = self.visit(ast.expr3, env).value
        if type(expr3) is not IntType:
            raise TypeMismatchInExpression(ast)

        new_env = []
        new_env = [self.visit(x, new_env) for x in ast.loop[0]] + new_env
        [self.visit(x, new_env + env) for x in ast.loop[1]]

    def visitBreak(self, ast, env):
        pass

    def visitContinue(self, ast, env):
        pass

    def findAndInferenceFunction(self, typ, env):
        for symbol in env:
            if isinstance(symbol.mtype.value, Function):
                if typ == None:
                    return symbol
                else:
                    if isinstance(symbol.returnType.value, Unknown):
                        symbol.returnType.value = typ.value
                        return True
                    if type(symbol.returnType.value) is type(typ.value):
                        return True
                    return False
        return False

    def visitReturn(self, ast, env):
        if type(ast.expr) is Id:
            name = self.visit(ast.expr, env)
            expr = self.findIdInEnv(name, env).mtype
            flag = self.findAndInferenceFunction(expr, env)
            if type(expr.value) is Unknown:
                raise TypeCannotBeInferred(ast)
            if not flag:
                raise TypeMismatchInStatement(ast)
            return expr

        expr = self.visit(ast.expr, env) if ast.expr else Wrapper(VoidType())
        flag = self.findAndInferenceFunction(expr, env)
        if type(expr.value) is Unknown:
            raise TypeCannotBeInferred(ast)
        if not flag:
            raise TypeMismatchInStatement(ast)
        return expr

    def visitDowhile(self, ast, env):
        new_env = []
        new_env = [self.visit(x, new_env) for x in ast.sl[0]] + new_env
        [self.visit(x, new_env + env) for x in ast.sl[1]]

        print(env)

        expr = self.visit(ast.exp, env)

        if type(ast.exp) is Id:
            expr = self.findIdInEnv(expr, env)
            exprType = expr.mtype
            if type(exprType.value) is Unknown:
                exprType.value = BoolType()
            if self.checkIfIdIsParam(expr.name, env):
                self.paramsTypeInference(expr, env)
            if not isinstance(exprType.value, BoolType):
                raise TypeMismatchInStatement(ast)
        else:
            if type(expr.value) is not BoolType:
                raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, env):
        expr = self.visit(ast.exp, env)
        if type(ast.exp) is Id:
            expr = self.findIdInEnv(expr, env)
            exprType = expr.mtype
            if type(exprType.value) is Unknown:
                exprType.value = BoolType()
            if self.checkIfIdIsParam(expr.name, env):
                self.paramsTypeInference(expr, env)
            if not isinstance(exprType.value, BoolType):
                raise TypeMismatchInStatement(ast)
        else:
            if type(expr.value) is not BoolType:
                raise TypeMismatchInStatement(ast)

        new_env = []
        new_env = [self.visit(x, new_env) for x in ast.sl[0]] + new_env
        [self.visit(x, new_env + env) for x in ast.sl[1]]

    def visitCallStmt(self, ast, env):
        method = self.visit(ast.method, env)
        callFunction = self.findFunctionInEnv(method, env)

        # function type can be inferred to VoidType
        if isinstance(callFunction.returnType.value, Unknown):
            callFunction.returnType.value = VoidType()

        if not isinstance(callFunction.returnType.value, VoidType):
            raise TypeMismatchInStatement(ast)

        envParams = callFunction.paramTypes.value
        callParamsNotFull = [self.visit(x, env) for x in ast.param]

        callParams = []
        for param in callParamsNotFull:
            if type(param) == str:
                callParams = [self.findIdInEnv(param, env).mtype] + callParams
            else:
                callParams = [param] + callParams

        if len(envParams) is not len(callParams):
            raise TypeMismatchInStatement(ast)
        else:
            for index in range(0, len(envParams)):
                if isinstance(callParams[index].value, Unknown) and isinstance(
                    envParams[index].mtype.value, Unknown
                ):
                    raise TypeCannotBeInferred(ast)
                if isinstance(envParams[index].mtype.value, Unknown):
                    envParams[index].mtype.value = callParams[index].value
                if isinstance(callParams[index].value, Unknown):
                    callParams[index].value = envParams[index].mtype.value
                if type(envParams[index].mtype.value) is type(callParams[index].value):
                    continue
                if type(envParams[index].mtype.value) is not type(
                    callParams[index].value
                ):
                    raise TypeMismatchInStatement(ast)
