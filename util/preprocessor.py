from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from freader import FileReader

class Preprocessor:
  def __init__(self, filePath, ngrams=1):
    self.reader = FileReader(filePath)
    self.ngrams = ngrams
    self.sentences = [ ]
    self.processed = [ ]
    self.paragraphStructure = { }
    self.sCount = 0
    self.pCount = 0

  def parse(self):
    self.reader.read( self.process )
    return self

  def process(self, paragraph):
    for sentence in sent_tokenize(paragraph):
      self.sentences.append( sentence )
      self.processed.append( map(lambda w: w[0], list(ngrams(word_tokenize(sentence), self.ngrams))) )

      self.paragraphStructure[self.sCount] = self.pCount
      self.sCount = self.sCount + 1

    self.pCount = self.pCount + 1



