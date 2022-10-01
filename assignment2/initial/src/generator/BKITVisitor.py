# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#full_variable.
    def visitFull_variable(self, ctx:BKITParser.Full_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_list.
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_name.
    def visitFunc_name(self, ctx:BKITParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_param.
    def visitFunc_param(self, ctx:BKITParser.Func_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_list.
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr_list.
    def visitExpr_list(self, ctx:BKITParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expr.
    def visitExpr(self, ctx:BKITParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logic_expr.
    def visitLogic_expr(self, ctx:BKITParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#add_expr.
    def visitAdd_expr(self, ctx:BKITParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mul_expr.
    def visitMul_expr(self, ctx:BKITParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#not_expr.
    def visitNot_expr(self, ctx:BKITParser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_expr.
    def visitSign_expr(self, ctx:BKITParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#element_expr.
    def visitElement_expr(self, ctx:BKITParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_expr.
    def visitFunc_expr(self, ctx:BKITParser.Func_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parenthesed_expr.
    def visitParenthesed_expr(self, ctx:BKITParser.Parenthesed_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_element.
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmts.
    def visitStmts(self, ctx:BKITParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#other_stmt.
    def visitOther_stmt(self, ctx:BKITParser.Other_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl_stmt.
    def visitVardecl_stmt(self, ctx:BKITParser.Vardecl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal_element.
    def visitLiteral_element(self, ctx:BKITParser.Literal_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)



del BKITParser