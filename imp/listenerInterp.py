import sys
from antlr4 import *
from imprwParser import imprwParser
from imprwListener import imprwListener

class ListenerInterp(imprwListener):
    assignments = 0

    def exitAssignStmt(self, ctx:imprwParser.AssignStmtContext):
        self.assignments += 1
        
    def exitProgr(self, ctx:imprwParser.ProgrContext):
        print(f"Assigned {self.assignments} times")
