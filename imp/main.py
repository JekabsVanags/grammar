import sys
import re
import nltk
from antlr4 import *
from antlr4.tree.Trees import Trees
from imprwLexer import imprwLexer
from imprwParser import imprwParser
from imprwVisitor import imprwVisitor
from listenerInterp import ListenerInterp
from imprwCompiler import imprwCompiler

def parseFile(input, drawTree):
  input_stream = FileStream(input)
  lexer = imprwLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = imprwParser(stream)
  tree = parser.progr()
  treeString = Trees.toStringTree(tree, None, parser)

  linterp = ListenerInterp()
  walker = ParseTreeWalker()
  walker.walk(linterp, tree)
  if drawTree:
    nltk.Tree.draw(nltk.Tree.fromstring(treeString))

def interpretFile(input):
  input_stream = FileStream(input)
  lexer = imprwLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = imprwParser(stream)
  tree = parser.progr()
  treeString = Trees.toStringTree(tree, None, parser)

  visitor = imprwVisitor()
  visitor.visitProgr(tree)

def compileFile(input):
  input_stream = FileStream(input)
  lexer = imprwLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = imprwParser(stream)
  tree = parser.progr()
  treeString = Trees.toStringTree(tree, None, parser)

  visitor = imprwCompiler()
  code = visitor.visitProgr(tree)
  
  print(code)    



def main(argv):
  
  #Change paramater to True to get the tree visualization
  # parseFile("/home/jekabsvanags/grammar/program1.txt", True)
  # parseFile("/home/jekabsvanags/grammar/program2.txt", True)
  # parseFile("/home/jekabsvanags/grammar/program3.txt", True)
  # parseFile("/home/jekabsvanags/grammar/program4.txt", True)
  # parseFile("/home/jekabsvanags/grammar/program5.txt", True)
  #parseFile("/home/jekabsvanags/grammar/imp/input.txt", True)

  #Interpret file input.txt with data.txt
  #NOTES: while loops end with od and for loops with fi (no end). Also =< is <=. 
  compileFile("/home/jekabsvanags/grammar/imp/input.txt")

if __name__ == '__main__':
  main(sys.argv)