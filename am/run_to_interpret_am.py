import nltk
from antlr4 import *
from antlr4.tree.Trees import Trees
from amLexer import amLexer
from amParser import amParser
from amVisitor import amVisitor


input_stream = FileStream("am/input.txt")
lexer = amLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = amParser(stream)
tree = parser.program()
treeString = Trees.toStringTree(tree, None, parser)

visitor = amVisitor()
visitor.visitProgram(tree)