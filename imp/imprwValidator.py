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

class imprwValidator(ParseTreeVisitor):

    ver_conditions = []
    intermediate_count = {"p": 1, "r": 1};
    full = False

    def visitProgr(self, ctx: imprwParser.ProgrContext, precondition, postcondition, full = False):
        self.full = full
        self.visitSeries(ctx.series(), precondition, postcondition)
        print(self.ver_conditions)

    def visitSeries(self, ctx: imprwParser.SeriesContext, precondition, postcondition):
        if(isinstance(ctx, list)):
            self.visitSeries(ctx[0], precondition, postcondition)
        else:
            self.visitStmt(ctx.stmt(), precondition, postcondition)


    def visitStmt(self, ctx: imprwParser.StmtContext, precondition, postcondition):
        if ctx.assignStmt():
            self.visitAssignStmt(ctx.assignStmt(), precondition, postcondition)
        elif ctx.condStmt():
            self.visitCondStmt(ctx.condStmt(), precondition, postcondition)
        elif ctx.loop():
            self.visitLoop(ctx.loop(), precondition, postcondition)
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == ';':
            if precondition[0] in self.intermediate_count.keys():
                intermediate = f"{precondition[0]}{self.intermediate_count[precondition[0]]}"
                self.intermediate_count[precondition[0]] += 1
            else:
                count = self.intermediate_count["r"]
                intermediate = f"r{count}"
                self.intermediate_count["r"] += 1

            self.visitStmt(ctx.getChild(0), precondition, intermediate)
            self.visitStmt(ctx.getChild(2), intermediate, postcondition)

    def visitAssignStmt(self, ctx: imprwParser.AssignStmtContext, precondition, postcondition):
        x = ctx.VARNAME().getText()
        a = self.visitExpr(ctx.expr())
        postcondition_prime = postcondition + f"[{a} / {x}]"
        self.ver_conditions.append(f"{precondition} ⇒ {postcondition_prime}")

    def visitCondStmt(self, ctx: imprwParser.CondStmtContext, precondition, postcondition):
        b = ctx.compar().getText()
        self.visitSeries(ctx.series(0), f"{precondition} ∧ {b}", postcondition)
        if ctx.series(1):
            self.visitSeries(ctx.series(1), f"{precondition} ∧ ¬{b}", postcondition)

    def visitLoop(self, ctx: imprwParser.LoopContext, precondition, postcondition):
        r = "r"
        v = "v"
        b = ctx.compar().getText()

        if ctx.anotation():
          r = ctx.anotation().compar().getText()
          if(ctx.anotation().expr()):
            v = ctx.anotation().expr().getText()
        
        print("Invariants:", r)
        print("Variants:", v)
          
        self.ver_conditions.append(f"{precondition} ⇒ {r}")
        if self.full:
            self.visitSeries(ctx.series(), f"({r} ∧ {b} ∧ {v} = X)", f"({r} ∧ 0 <= {v} ∧ {v} < X)")
        else:
            self.visitSeries(ctx.series(), f"{r} ∧ {b}", r)
        self.ver_conditions.append(f"{r} ∧ ¬{b} ⇒ {postcondition}")

    def visitExpr(self, ctx: imprwParser.ExprContext):
        return ctx.getText()
