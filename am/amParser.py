# Generated from am.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3")
        buf.write("\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\5\4$\n\4\3\5\3\5\3")
        buf.write("\5\3\5\5\5*\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\5\n<\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\2\3\3\2\3\16\2D\2\30\3\2\2\2\4\32\3")
        buf.write("\2\2\2\6#\3\2\2\2\b)\3\2\2\2\n+\3\2\2\2\f-\3\2\2\2\16")
        buf.write("\61\3\2\2\2\20\65\3\2\2\2\22;\3\2\2\2\24=\3\2\2\2\26C")
        buf.write("\3\2\2\2\30\31\5\4\3\2\31\3\3\2\2\2\32\36\5\6\4\2\33\35")
        buf.write("\5\6\4\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37\5\3\2\2\2 \36\3\2\2\2!$\5\b\5\2\"$\5\22\n")
        buf.write("\2#!\3\2\2\2#\"\3\2\2\2$\7\3\2\2\2%*\5\f\7\2&*\5\16\b")
        buf.write("\2\'*\5\20\t\2(*\5\n\6\2)%\3\2\2\2)&\3\2\2\2)\'\3\2\2")
        buf.write("\2)(\3\2\2\2*\t\3\2\2\2+,\t\2\2\2,\13\3\2\2\2-.\7\17\2")
        buf.write("\2./\7\26\2\2/\60\7\20\2\2\60\r\3\2\2\2\61\62\7\21\2\2")
        buf.write("\62\63\7\27\2\2\63\64\7\20\2\2\64\17\3\2\2\2\65\66\7\22")
        buf.write("\2\2\66\67\7\26\2\2\678\7\20\2\28\21\3\2\2\29<\5\24\13")
        buf.write("\2:<\5\26\f\2;9\3\2\2\2;:\3\2\2\2<\23\3\2\2\2=>\7\23\2")
        buf.write("\2>?\5\4\3\2?@\7\24\2\2@A\5\4\3\2AB\7\20\2\2B\25\3\2\2")
        buf.write("\2CD\7\25\2\2DE\5\4\3\2EF\7\24\2\2FG\5\4\3\2GH\7\20\2")
        buf.write("\2H\27\3\2\2\2\6\36#);")
        return buf.getvalue()


class amParser ( Parser ):

    grammarFileName = "am.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ADD'", "'MULT'", "'SUB'", "'DIV'", "'TRUE'", 
                     "'FALSE'", "'EQ'", "'LE'", "'AND'", "'OR'", "'NEG'", 
                     "'NOOP'", "'FETCH('", "')'", "'PUSH('", "'STORE('", 
                     "'BRANCH('", "','", "'LOOP('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VARIABLE", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_prog = 1
    RULE_statement = 2
    RULE_simple = 3
    RULE_simple_commands = 4
    RULE_fetch = 5
    RULE_push = 6
    RULE_store = 7
    RULE_complexStatement = 8
    RULE_branch = 9
    RULE_loop = 10

    ruleNames =  [ "program", "prog", "statement", "simple", "simple_commands", 
                   "fetch", "push", "store", "complexStatement", "branch", 
                   "loop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    VARIABLE=20
    NUMBER=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(amParser.ProgContext,0)


        def getRuleIndex(self):
            return amParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = amParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.prog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amParser.StatementContext)
            else:
                return self.getTypedRuleContext(amParser.StatementContext,i)


        def getRuleIndex(self):
            return amParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = amParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.statement()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amParser.T__0) | (1 << amParser.T__1) | (1 << amParser.T__2) | (1 << amParser.T__3) | (1 << amParser.T__4) | (1 << amParser.T__5) | (1 << amParser.T__6) | (1 << amParser.T__7) | (1 << amParser.T__8) | (1 << amParser.T__9) | (1 << amParser.T__10) | (1 << amParser.T__11) | (1 << amParser.T__12) | (1 << amParser.T__14) | (1 << amParser.T__15) | (1 << amParser.T__16) | (1 << amParser.T__18))) != 0):
                self.state = 25
                self.statement()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(amParser.SimpleContext,0)


        def complexStatement(self):
            return self.getTypedRuleContext(amParser.ComplexStatementContext,0)


        def getRuleIndex(self):
            return amParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = amParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [amParser.T__0, amParser.T__1, amParser.T__2, amParser.T__3, amParser.T__4, amParser.T__5, amParser.T__6, amParser.T__7, amParser.T__8, amParser.T__9, amParser.T__10, amParser.T__11, amParser.T__12, amParser.T__14, amParser.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.simple()
                pass
            elif token in [amParser.T__16, amParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.complexStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fetch(self):
            return self.getTypedRuleContext(amParser.FetchContext,0)


        def push(self):
            return self.getTypedRuleContext(amParser.PushContext,0)


        def store(self):
            return self.getTypedRuleContext(amParser.StoreContext,0)


        def simple_commands(self):
            return self.getTypedRuleContext(amParser.Simple_commandsContext,0)


        def getRuleIndex(self):
            return amParser.RULE_simple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple" ):
                listener.enterSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple" ):
                listener.exitSimple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = amParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [amParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.fetch()
                pass
            elif token in [amParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.push()
                pass
            elif token in [amParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.store()
                pass
            elif token in [amParser.T__0, amParser.T__1, amParser.T__2, amParser.T__3, amParser.T__4, amParser.T__5, amParser.T__6, amParser.T__7, amParser.T__8, amParser.T__9, amParser.T__10, amParser.T__11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.simple_commands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_commandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return amParser.RULE_simple_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_commands" ):
                listener.enterSimple_commands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_commands" ):
                listener.exitSimple_commands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_commands" ):
                return visitor.visitSimple_commands(self)
            else:
                return visitor.visitChildren(self)




    def simple_commands(self):

        localctx = amParser.Simple_commandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << amParser.T__0) | (1 << amParser.T__1) | (1 << amParser.T__2) | (1 << amParser.T__3) | (1 << amParser.T__4) | (1 << amParser.T__5) | (1 << amParser.T__6) | (1 << amParser.T__7) | (1 << amParser.T__8) | (1 << amParser.T__9) | (1 << amParser.T__10) | (1 << amParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FetchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(amParser.VARIABLE, 0)

        def getRuleIndex(self):
            return amParser.RULE_fetch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFetch" ):
                listener.enterFetch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFetch" ):
                listener.exitFetch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFetch" ):
                return visitor.visitFetch(self)
            else:
                return visitor.visitChildren(self)




    def fetch(self):

        localctx = amParser.FetchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fetch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(amParser.T__12)
            self.state = 44
            self.match(amParser.VARIABLE)
            self.state = 45
            self.match(amParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PushContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(amParser.NUMBER, 0)

        def getRuleIndex(self):
            return amParser.RULE_push

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPush" ):
                listener.enterPush(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPush" ):
                listener.exitPush(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPush" ):
                return visitor.visitPush(self)
            else:
                return visitor.visitChildren(self)




    def push(self):

        localctx = amParser.PushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(amParser.T__14)
            self.state = 48
            self.match(amParser.NUMBER)
            self.state = 49
            self.match(amParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StoreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(amParser.VARIABLE, 0)

        def getRuleIndex(self):
            return amParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStore" ):
                return visitor.visitStore(self)
            else:
                return visitor.visitChildren(self)




    def store(self):

        localctx = amParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(amParser.T__15)
            self.state = 52
            self.match(amParser.VARIABLE)
            self.state = 53
            self.match(amParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComplexStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def branch(self):
            return self.getTypedRuleContext(amParser.BranchContext,0)


        def loop(self):
            return self.getTypedRuleContext(amParser.LoopContext,0)


        def getRuleIndex(self):
            return amParser.RULE_complexStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexStatement" ):
                listener.enterComplexStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexStatement" ):
                listener.exitComplexStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexStatement" ):
                return visitor.visitComplexStatement(self)
            else:
                return visitor.visitChildren(self)




    def complexStatement(self):

        localctx = amParser.ComplexStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_complexStatement)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [amParser.T__16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.branch()
                pass
            elif token in [amParser.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BranchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amParser.ProgContext)
            else:
                return self.getTypedRuleContext(amParser.ProgContext,i)


        def getRuleIndex(self):
            return amParser.RULE_branch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch" ):
                listener.enterBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch" ):
                listener.exitBranch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch" ):
                return visitor.visitBranch(self)
            else:
                return visitor.visitChildren(self)




    def branch(self):

        localctx = amParser.BranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_branch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(amParser.T__16)
            self.state = 60
            self.prog()
            self.state = 61
            self.match(amParser.T__17)
            self.state = 62
            self.prog()
            self.state = 63
            self.match(amParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(amParser.ProgContext)
            else:
                return self.getTypedRuleContext(amParser.ProgContext,i)


        def getRuleIndex(self):
            return amParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = amParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(amParser.T__18)
            self.state = 66
            self.prog()
            self.state = 67
            self.match(amParser.T__17)
            self.state = 68
            self.prog()
            self.state = 69
            self.match(amParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





