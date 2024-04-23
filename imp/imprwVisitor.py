# Generated from imprw.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .imprwParser import imprwParser
else:
    from imprwParser import imprwParser

# This class defines a complete generic visitor for a parse tree produced by imprwParser.

class imprwVisitor(ParseTreeVisitor):

    state = {}

    with open('imp/data.txt', 'r') as file:
        input_values = file.readline().strip()
            
    input_values = input_values.split(',')

    def visitProgr(self, ctx: imprwParser.ProgrContext):
        self.visitSeries(ctx.series())
        
    def visitSeries(self, ctx: imprwParser.SeriesContext):
        if(isinstance(ctx, list)):
            self.visitSeries(ctx[0])
        else:
            self.visitStmt(ctx.stmt())
 
    def visitStmt(self, ctx: imprwParser.StmtContext):
        if ctx.inputStmt():
            self.visitInputStmt(ctx.inputStmt())
        elif ctx.outputStmt():
            self.visitOutputStmt(ctx.outputStmt())
        elif ctx.assignStmt():
            self.visitAssignStmt(ctx.assignStmt())
        elif ctx.condStmt():
            self.visitCondStmt(ctx.condStmt())
        elif ctx.loop():
            self.visitLoop(ctx.loop())
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == ';':
            self.visitStmt(ctx.getChild(0))
            self.visitStmt(ctx.getChild(2))

    def visitInputStmt(self, ctx: imprwParser.InputStmtContext):
        variables = self.visitVarlist(ctx.varlist())

        for var in variables:
            self.state[var] = int(self.input_values[0])
            del self.input_values[0]


    def visitOutputStmt(self, ctx: imprwParser.OutputStmtContext):
        variables = self.visitVarlist(ctx.varlist())
        for var in variables:
            value = self.state[var]
            print(var, ":", value)
       

    def visitAssignStmt(self, ctx: imprwParser.AssignStmtContext):
        variable = ctx.VARNAME().getText()
        value = self.visitExpr(ctx.expr())

        self.state[variable] = value

    def visitCondStmt(self, ctx: imprwParser.CondStmtContext):
        compar = self.visitCompar(ctx.compar())
        if compar:
            self.visitSeries(ctx.series(0))
        elif ctx.series(1):
            self.visitSeries(ctx.series(1))

    def visitLoop(self, ctx: imprwParser.LoopContext):
        condition = self.visitCompar(ctx.compar())
        while condition:
            self.visitSeries(ctx.series())
            condition = self.visitCompar(ctx.compar())

    def visitCompar(self, ctx: imprwParser.ComparContext):
        if(ctx.compar()):
            return self.visitCompar(ctx.compar()) or self.visitComparterm(ctx.comparterm())
        else:
            return self.visitComparterm(ctx.comparterm())

    def visitComparterm(self, ctx: imprwParser.CompartermContext):
        if(ctx.comparterm()):
            return self.visitComparterm(ctx.comparterm()) and self.visitComparelem(ctx.comparelem())
        else:
            return self.visitComparelem(ctx.comparelem())

    def visitComparelem(self, ctx: imprwParser.ComparelemContext):
        if(ctx.compar()):
            return not self.visitCompar(ctx.compar())
        elif(ctx.RELATION()):
            relation = ctx.RELATION().getText()
            expr = ctx.expr()
            left_side = self.visitExpr(expr[0])
            right_side = self.visitExpr(expr[1])
            
            if relation == '=':
                return left_side == right_side
            elif relation == '<>':
                return left_side != right_side
            elif relation == '<':
                return left_side < right_side
            elif relation == '>':
                return left_side > right_side
            elif relation == '<=':
                return left_side <= right_side
            elif relation == '>=':
                return left_side >= right_side
        else:
            value = self.visitExpr(expr[0])
            if(value):
                return True
            else:
                return False




    def visitVarlist(self, ctx: imprwParser.VarlistContext):
        variables = []
        for variable in ctx.VARNAME():
            variables.append(variable.getText())
        return variables

    def visitExpr(self, ctx: imprwParser.ExprContext):
        w_op = ctx.WEAKOP()
        if(w_op):
            operator = w_op.getText()
            if operator == "+":
                return self.visitExpr(ctx.expr()) + self.visitTerm(ctx.term())
            elif operator == "-":
                return self.visitExpr(ctx.expr()) - self.visitTerm(ctx.term())
        else:
            return self.visitTerm(ctx.term())

    def visitTerm(self, ctx: imprwParser.TermContext):
        s_op = ctx.STRONGOP()
        if(s_op):
            operator = s_op.getText()
            if operator == "*":
                return self.visitTerm(ctx.term()) * self.visitElem(ctx.elem())
            elif operator == "/":
                return self.visitTerm(ctx.term()) / self.visitElem(ctx.elem())
        else:
            return self.visitElem(ctx.elem())

    def visitElem(self, ctx: imprwParser.ElemContext):
        value = None
        if(ctx.VARNAME()):
            var = ctx.VARNAME().getText()
            value = self.state[var]
        elif(ctx.NUMBER()):
            value = ctx.NUMBER().getText()
            value = int(value)
        elif(ctx.TRUTHVAL()):
            val = ctx.VARNAME().getText()
            if val == "true":
                value = True
            elif val == "false":
                value = False
        elif(ctx.expr()):
            value = self.visitExpr(ctx.expr())

        return value



del imprwParser