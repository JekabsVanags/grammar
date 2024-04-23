# Generated from am.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .amParser import amParser
else:
    from amParser import amParser

# This class defines a complete generic visitor for a parse tree produced by amParser.

class amVisitor(ParseTreeVisitor):

    stack = []
    state = {}

    # Visit a parse tree produced by amParser#program.
    def visitProgram(self, ctx:amParser.ProgramContext):
        self.visitChildren(ctx)
        print("STATE:", self.state)

    # Visit a parse tree produced by amParser#prog.
    def visitProg(self, ctx:amParser.ProgContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by amParser#statement.
    def visitStatement(self, ctx:amParser.StatementContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by amParser#simple.
    def visitSimple(self, ctx:amParser.SimpleContext):
        command = ctx.simple_commands()
        if command:
            command = command.getText()
            if(command == "ADD"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 + n2)
            elif(command == "MULT"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 * n2)
            elif(command == "SUB"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n2 - n1)
            elif(command == "DIV"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n2 / n1)
            elif(command == "TRUE"):
                self.stack.append(True)
            elif(command == "FALSE"):
                self.stack.append(False)
            elif(command == "EQ"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 == n2) 
            elif(command == "LE"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 >= n2)
            elif(command == "AND"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 and n2) 
            elif(command == "OR"):
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                self.stack.append(n1 or n2)   
            elif(command == "NEG"):
                n1 = self.stack.pop()
                self.stack.append(not n1)  
            elif(command == "NOOP"):
                pass
        else:
            self.visitChildren(ctx)

      # Visit a parse tree produced by amParser#fetch.
    def visitFetch(self, ctx:amParser.FetchContext):
        var = ctx.VARIABLE().getText()
        self.stack.append(self.state[var])


    # Visit a parse tree produced by amParser#push.
    def visitPush(self, ctx:amParser.PushContext):
        nr = int(ctx.NUMBER().getText())
        self.stack.append(nr)


    # Visit a parse tree produced by amParser#store.
    def visitStore(self, ctx:amParser.StoreContext):
        var = ctx.VARIABLE().getText()
        self.state[var] = self.stack.pop()


    # Visit a parse tree produced by amParser#complexStatement.
    def visitComplexStatement(self, ctx:amParser.ComplexStatementContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by amParser#branch.
    def visitBranch(self, ctx:amParser.BranchContext):
        prog = ctx.prog()
        if self.stack.pop() == True:
            self.visitProg(prog[0])
        else:
            self.visitProg(prog[1])

    # Visit a parse tree produced by amParser#loop.
    def visitLoop(self, ctx:amParser.LoopContext):
        prog = ctx.prog()
        self.visitProg(prog[0])
        condition = self.stack.pop()
        while(condition):
            self.visitProg(prog[1])
            self.visitProg(prog[0])
            condition = self.stack.pop()



del amParser