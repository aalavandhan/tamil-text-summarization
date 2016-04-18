from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from freader import FileReader

class Preprocessor:
  def __init__(self, filePath, ngrams=1):
    self.reader = FileReader(filePath)
    self.ngrams = ngrams
    self.sentences = [ ]
    self.processed = [ ]
    self.sCount = 0

  def parse(self):
    self.reader.read( self.process )
    return self

  def process(self, line):
    for sentence in sent_tokenize(line):
      self.sentences.append( sentence )
      self.processed.append( list(ngrams(word_tokenize(sentence), self.ngrams)) )
      self.sCount = self.sCount + 1



