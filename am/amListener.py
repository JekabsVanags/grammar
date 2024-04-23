# Generated from am.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .amParser import amParser
else:
    from amParser import amParser

# This class defines a complete listener for a parse tree produced by amParser.
class amListener(ParseTreeListener):

    # Enter a parse tree produced by amParser#program.
    def enterProgram(self, ctx:amParser.ProgramContext):
        pass

    # Exit a parse tree produced by amParser#program.
    def exitProgram(self, ctx:amParser.ProgramContext):
        pass


    # Enter a parse tree produced by amParser#prog.
    def enterProg(self, ctx:amParser.ProgContext):
        pass

    # Exit a parse tree produced by amParser#prog.
    def exitProg(self, ctx:amParser.ProgContext):
        pass


    # Enter a parse tree produced by amParser#statement.
    def enterStatement(self, ctx:amParser.StatementContext):
        pass

    # Exit a parse tree produced by amParser#statement.
    def exitStatement(self, ctx:amParser.StatementContext):
        pass


    # Enter a parse tree produced by amParser#simple.
    def enterSimple(self, ctx:amParser.SimpleContext):
        pass

    # Exit a parse tree produced by amParser#simple.
    def exitSimple(self, ctx:amParser.SimpleContext):
        pass


    # Enter a parse tree produced by amParser#simple_commands.
    def enterSimple_commands(self, ctx:amParser.Simple_commandsContext):
        pass

    # Exit a parse tree produced by amParser#simple_commands.
    def exitSimple_commands(self, ctx:amParser.Simple_commandsContext):
        pass


    # Enter a parse tree produced by amParser#fetch.
    def enterFetch(self, ctx:amParser.FetchContext):
        pass

    # Exit a parse tree produced by amParser#fetch.
    def exitFetch(self, ctx:amParser.FetchContext):
        pass


    # Enter a parse tree produced by amParser#push.
    def enterPush(self, ctx:amParser.PushContext):
        pass

    # Exit a parse tree produced by amParser#push.
    def exitPush(self, ctx:amParser.PushContext):
        pass


    # Enter a parse tree produced by amParser#store.
    def enterStore(self, ctx:amParser.StoreContext):
        pass

    # Exit a parse tree produced by amParser#store.
    def exitStore(self, ctx:amParser.StoreContext):
        pass


    # Enter a parse tree produced by amParser#complexStatement.
    def enterComplexStatement(self, ctx:amParser.ComplexStatementContext):
        pass

    # Exit a parse tree produced by amParser#complexStatement.
    def exitComplexStatement(self, ctx:amParser.ComplexStatementContext):
        pass


    # Enter a parse tree produced by amParser#branch.
    def enterBranch(self, ctx:amParser.BranchContext):
        pass

    # Exit a parse tree produced by amParser#branch.
    def exitBranch(self, ctx:amParser.BranchContext):
        pass


    # Enter a parse tree produced by amParser#loop.
    def enterLoop(self, ctx:amParser.LoopContext):
        pass

    # Exit a parse tree produced by amParser#loop.
    def exitLoop(self, ctx:amParser.LoopContext):
        pass


