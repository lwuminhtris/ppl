# 1811298


from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    def flatten(self, l: list):
        if l == []:
            return []
        else:
            return reduce(lambda x, y: x + y, l)

    def int_convert(self, s: str):
        if "x" in s or "X" in s:
            return int(s, 16)
        elif "o" in s or "O" in s:
            return int(s, 8)
        else:
            return int(s)

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        vardecls = [] if not ctx.var_decl() else [self.visit(x) for x in ctx.var_decl()]
        funcdecls = (
            [] if not ctx.func_decl() else [self.visit(x) for x in ctx.func_decl()]
        )
        decls = self.flatten(vardecls) + self.flatten(funcdecls)
        # return Program(decl=decls)
        return Program(decls)

    def visitVar_decl(self, ctx: BKITParser.Var_declContext):
        return self.visit(ctx.variable_list())

    def visitVariable(self, ctx: BKITParser.VariableContext):
        var = Id(ctx.ID().getText())
        dimen = (
            [self.int_convert(x.getText()) for x in ctx.INT_LIT()]
            if ctx.INT_LIT()
            else []
        )
        return (var, dimen)

    def visitFull_variable(self, ctx: BKITParser.Full_variableContext):
        var, dimen = self.visit(ctx.variable())
        init = self.visitLiteral(ctx.literal()) if ctx.literal() else None
        # return VarDecl(variable=var, varDimen=dimen, varInit=init)
        return VarDecl(var, dimen, init)

    def visitVariable_list(self, ctx: BKITParser.Variable_listContext):
        return [self.visit(x) for x in ctx.full_variable()]

    def visitFunc_decl(self, ctx: BKITParser.Func_declContext):
        name = self.visit(ctx.func_name())
        param = self.visit(ctx.func_param()) if ctx.func_param() else []
        body = self.visit(ctx.func_body())
        # return [FuncDecl(name=name, param=param, body=body)]
        return [FuncDecl(name, param, body)]

    def visitFunc_name(self, ctx: BKITParser.Func_nameContext):
        return Id(ctx.ID().getText())

    def visitFunc_param(self, ctx: BKITParser.Func_paramContext):
        return self.visit(ctx.param_list())

    def visitFunc_body(self, ctx: BKITParser.Func_bodyContext):
        vardecl_stmts, other_stmts = self.visit(ctx.stmts())
        return (vardecl_stmts, other_stmts)

    def visitParam_list(self, ctx: BKITParser.Param_listContext):
        return [
            # VarDecl(variable=self.visit(x)[0], varDimen=self.visit(x)[1], varInit=None)
            VarDecl(self.visit(x)[0], self.visit(x)[1], None)
            for x in ctx.variable()
        ]

    # Expressions

    def visitExpr_list(self, ctx: BKITParser.Expr_listContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitExpr(self, ctx: BKITParser.ExprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            # return BinaryOp(op=op, left=lhs, right=rhs)
            return BinaryOp(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitLogic_expr(self, ctx: BKITParser.Logic_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            # return BinaryOp(op=op, left=lhs, right=rhs)
            return BinaryOp(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitAdd_expr(self, ctx: BKITParser.Add_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            # return BinaryOp(op=op, left=lhs, right=rhs)
            return BinaryOp(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitMul_expr(self, ctx: BKITParser.Mul_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            # return BinaryOp(op=op, left=lhs, right=rhs)
            return BinaryOp(op, lhs, rhs)
        else:
            return self.visit(ctx.getChild(0))

    def visitNot_expr(self, ctx: BKITParser.Not_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            # return UnaryOp(op=op, body=body)
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.getChild(0))

    def visitSign_expr(self, ctx: BKITParser.Sign_exprContext):
        if ctx.getChildCount() > 1:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.getChild(1))
            # return UnaryOp(op=op, body=body)
            return UnaryOp(op, body)
        else:
            return self.visit(ctx.getChild(0))

    def visitElement_expr(self, ctx: BKITParser.Element_exprContext):
        return self.visit(ctx.getChild(0))

    def visitFunc_expr(self, ctx: BKITParser.Func_exprContext):
        return self.visit(ctx.getChild(0))

    def visitParenthesed_expr(self, ctx: BKITParser.Parenthesed_exprContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            return Id(ctx.ID().getText())

    def visitFunc_call(self, ctx: BKITParser.Func_callContext):
        name = Id(ctx.ID().getText())
        exprs = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        # return CallExpr(method=name, param=exprs)
        return CallExpr(name, exprs)

    def visitIndex_operators(self, ctx: BKITParser.Index_operatorsContext):
        if ctx.index_operators():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_operators())
        else:
            return [self.visit(ctx.expr())]

    def visitArray_element(self, ctx: BKITParser.Array_elementContext):
        arr = self.visit(ctx.getChild(0))
        idx = self.visit(ctx.index_operators())
        # return ArrayCell(arr=arr, idx=idx)
        return ArrayCell(arr, idx)

    # Statements

    def visitStmts(self, ctx: BKITParser.StmtsContext):
        vardecl_stmts = (
            []
            if not ctx.vardecl_stmt()
            else self.flatten([self.visit(x) for x in ctx.vardecl_stmt()])
        )
        other_stmts = (
            [] if not ctx.other_stmt() else [self.visit(x) for x in ctx.other_stmt()]
        )
        return (vardecl_stmts, other_stmts)

    def visitOther_stmt(self, ctx: BKITParser.Other_stmtContext):
        return self.visit(ctx.getChild(0))

    def visitVardecl_stmt(self, ctx: BKITParser.Vardecl_stmtContext):
        return self.visit(ctx.var_decl())

    def visitAssign_stmt(self, ctx: BKITParser.Assign_stmtContext):
        lhs = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.array_element())
        rhs = self.visit(ctx.expr())
        # return Assign(lhs=lhs, rhs=rhs)
        return Assign(lhs, rhs)

    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        exprs = [self.visit(x) for x in ctx.expr()]
        stmts = [self.visit(x) for x in ctx.stmts()]
        ifthenStmts = list(map(lambda x: [x[0]] + list(x[1]), zip(exprs, stmts)))
        elseStmt = stmts[-1] if ctx.ELSE() else ([], [])
        # return If(ifthenStmt=ifThenStmts, elseStmt=elseStmt)
        return If(ifthenStmts, elseStmt)

    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        idx1 = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        expr3 = self.visit(ctx.expr(2))
        loop = self.visit(ctx.stmts())
        # return For(idx1=name, expr1=expr1, expr2=expr2, expr3=expr3, loop=loop)
        return For(idx1, expr1, expr2, expr3, loop)

    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        expr = self.visit(ctx.expr())
        sl = self.visit(ctx.stmts())
        # return While(exp=expr, sl=sl)
        return While(expr, sl)

    def visitDo_while_stmt(self, ctx: BKITParser.Do_while_stmtContext):
        expr = self.visit(ctx.expr())
        sl = self.visit(ctx.stmts())
        # return Dowhile(exp=expr, sl=sl)
        return Dowhile(sl, expr)

    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKITParser.Continue_stmtContext):
        return Continue()

    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        func_call = self.visit(ctx.func_call())
        # return CallStmt(method=func_call.method, param=func_call.param)
        return CallStmt(func_call.method, func_call.param)

    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        # return Return(expr=expr)
        return Return(expr)

    def visitArray(self, ctx: BKITParser.ArrayContext):
        value = self.visit(ctx.literal_element())
        # return ArrayLiteral(value=self.visit(ctx.literal_element()))
        return ArrayLiteral(value)

    def visitLiteral_element(
        self, ctx: BKITParser.Literal_elementContext
    ):
        return [self.visit(x) for x in ctx.literal()]

    def visitLiteral(self, ctx: BKITParser.LiteralContext):
        if ctx.INT_LIT():
            value = self.int_convert(ctx.INT_LIT().getText())
            # return IntLiteral(value=self.int_convert(ctx.INT_LIT().getText()))
            return IntLiteral(value)
        elif ctx.FLOAT_LIT():
            value = float(ctx.FLOAT_LIT().getText())
            # return FloatLiteral(value=float(ctx.FLOAT_LIT().getText()))
            return FloatLiteral(value)
        elif ctx.STRING_LIT():
            value = ctx.STRING_LIT().getText()
            # return StringLiteral(value=ctx.STRING_LIT().getText())
            return StringLiteral(value)
        elif ctx.BOOL_LIT():
            value = True if ctx.BOOL_LIT().getText() == "True" else False
            # return BooleanLiteral(value=value)
            return BooleanLiteral(value)
        else:
            return self.visit(ctx.array())
