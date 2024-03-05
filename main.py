import sys
import nltk 
from antlr4 import *
from antlr4.tree.Trees import Trees
from imprwLexer import imprwLexer
from imprwParser import imprwParser
from listenerInterp import ListenerInterp

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

def main(argv):
  #Change paramater to True to get the tree visualization
  parseFile("/home/jekabsvanags/grammar/program1.txt", True)
  parseFile("/home/jekabsvanags/grammar/program2.txt", True)
  parseFile("/home/jekabsvanags/grammar/program3.txt", True)
  parseFile("/home/jekabsvanags/grammar/program4.txt", True)
  parseFile("/home/jekabsvanags/grammar/program5.txt", True)

if __name__ == '__main__':
  main(sys.argv)