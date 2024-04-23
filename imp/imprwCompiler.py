# Generated from imprw.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .imprwParser import imprwParser
else:
    from imprwParser import imprwParser

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

class imprwCompiler(ParseTreeVisitor):

    code = []


    def visitProgr(self, ctx: imprwParser.ProgrContext):
        self.code = self.visitSeries(ctx.series())
        return  (" ").join(flatten(self.code))

    def visitSeries(self, ctx: imprwParser.SeriesContext):
        statements = []

        if(isinstance(ctx, list)):
            statements.append(self.visitSeries(ctx[0]))
        elif ctx and ctx.stmt():
            statements.append(self.visitStmt(ctx.stmt()))

        return statements
 
    def visitStmt(self, ctx: imprwParser.StmtContext):
        if ctx.inputStmt():
            return self.visitInputStmt(ctx.inputStmt())
        elif ctx.outputStmt():
            return self.visitOutputStmt(ctx.outputStmt())
        elif ctx.assignStmt():
            return self.visitAssignStmt(ctx.assignStmt())
        elif ctx.condStmt():
            return self.visitCondStmt(ctx.condStmt())
        elif ctx.loop():
            return self.visitLoop(ctx.loop())
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == ';':
            statements = []
            statements.append(self.visitStmt(ctx.getChild(0)))
            statements.append(self.visitStmt(ctx.getChild(2)))
            return statements

    def visitInputStmt(self, ctx: imprwParser.InputStmtContext):
        pass

    def visitOutputStmt(self, ctx: imprwParser.OutputStmtContext):
        pass
       
    def visitAssignStmt(self, ctx: imprwParser.AssignStmtContext):
        variable = ctx.VARNAME().getText()
        e = self.visitExpr(ctx.expr())
        return([e, f"STORE({variable})"])

    def visitCondStmt(self, ctx: imprwParser.CondStmtContext):
        c = self.visitCompar(ctx.compar())
        s1 = " ".join(flatten(self.visitSeries(ctx.series(0))))
        s2 = " ".join(flatten(self.visitSeries(ctx.series(1))))
        if s2 != "":
            return([c, f"BRANCH({s1},{s2})"])
        else:
            return([c, f"BRANCH({s1}, NOOP)"]) 
        

    def visitLoop(self, ctx: imprwParser.LoopContext):
        c = " ".join(flatten(self.visitCompar(ctx.compar())))
        s = " ".join(flatten(self.visitSeries(ctx.series())))
        return(f"LOOP({c},{s})")

    def visitCompar(self, ctx: imprwParser.ComparContext):
        if(ctx.compar()):
            self.visitCompar(ctx.compar())
            self.visitComparterm(ctx.comparterm())
            return("AND")
        else:
            return self.visitComparterm(ctx.comparterm())

    def visitComparterm(self, ctx: imprwParser.CompartermContext):
        if(ctx.comparterm()):
            self.visitComparterm(ctx.comparterm())
            self.visitComparelem(ctx.comparelem())
            return("OR")
        else:
            return self.visitComparelem(ctx.comparelem())

    def visitComparelem(self, ctx: imprwParser.ComparelemContext):
        if(ctx.compar()):
            c = self.visitCompar(ctx.compar())
            return([c, "NEG"])
        elif(ctx.RELATION()):
            relation = ctx.RELATION().getText()
            expr = ctx.expr()
            c1 = self.visitExpr(expr[0])
            c2 = self.visitExpr(expr[1])
            if relation == '=':
                return([c1, c2, "EQ"])
            elif relation == '<>':
                return([c1, c2, "EQ", "NEG"])
            elif relation == '<':
                return([c1, c2, "EQ", "NEG", c1, c2, "LE", "AND"])
            elif relation == '>':
                return([c1, c2, "LE", "NEG"])
            elif relation == '<=':
                return([c1, c2, "LE"])
            elif relation == '>=':
                return([c1, c2, "LE", "NEG", c1, c2, "EQ", "OR"])
        else:
            c = self.visitExpr(ctx.expr())
            return([c, "TRUE"])

    def visitVarlist(self, ctx: imprwParser.VarlistContext):
        pass

    def visitExpr(self, ctx: imprwParser.ExprContext):
        w_op = ctx.WEAKOP()
        if(w_op):
            e = self.visitExpr(ctx.expr())
            t = self.visitTerm(ctx.term())
            operator = w_op.getText()
            if operator == "+":
                return([e, t, "ADD"])
            elif operator == "-":
                return([e, t, "SUB"])
        else:
            return self.visitTerm(ctx.term())

    def visitTerm(self, ctx: imprwParser.TermContext):
        s_op = ctx.STRONGOP()
        if(s_op):
            t = self.visitTerm(ctx.term())
            e = self.visitElem(ctx.elem())
            operator = s_op.getText()
            if operator == "*":
                return([t, e, "MULT"])
            elif operator == "/":
                return([t, e, "DIV"])
        else:
            return self.visitElem(ctx.elem())

    def visitElem(self, ctx: imprwParser.ElemContext):
        if(ctx.VARNAME()):
            var = ctx.VARNAME().getText()
            return (f"FETCH({var})")
        elif(ctx.NUMBER()):
            value = ctx.NUMBER().getText()
            value = int(value)
            return(f"PUSH({value})")
        elif(ctx.TRUTHVAL()):
            val = ctx.VARNAME().getText()
            if val == "true":
                return("TRUE")
            elif val == "false":
                return("FALSE")
        elif(ctx.expr()):
            return self.visitExpr(ctx.expr())

