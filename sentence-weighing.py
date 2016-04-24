import sys
import operator
import math
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter

from util.distance     import editDistance

PATH = sys.argv[1]
SIZE = int(sys.argv[2]) if len(sys.argv) > 2 else 3


class SentenceScoreCalculator:
  def __init__(self, p):
    self.sCount = p.sCount
    self.counter = WordCounter(p.sCount).count(p.processed)
    self.vocabulary = self.counter.wordDict.keys()
    self.nWords = len(self.vocabulary)
    self.sentences = p.sentences
    self.calcuateEditDistance()

  def calcuateEditDistance(self):
  	self.lsw = { }

  	for s in range(self.sCount):
  		maxLen = lambda s2: max(len(self.sentences[s]), len(self.sentences[s2]))
  		ed = lambda s2: editDistance(self.sentences[s], self.sentences[s2])
  		lsw = lambda s2: float(maxLen(s2) - ed(s2)) / maxLen(s2)

  		self.lsw[s] = sum(map(lsw, range(self.sCount)))

  def sentenceWeight(self, index):
    words = self.counter.sentenceDict[index].keys()
    additionalOccurances = lambda w: ( self.counter.wordDict[w] - self.counter.sentenceDict[index][w] )

    return reduce(lambda s, w: additionalOccurances(w) / self.nWords, words, 0)

  def rank(self, index):
  	return(self.sentenceWeight(index) + self.lsw[index])

p = Preprocessor(PATH, 1).parse()
scorer = SentenceScoreCalculator(p)

summary = sorted(
  sorted(
    range(p.sCount), key=lambda s: scorer.rank(s), reverse=True)[0:SIZE])

for s in summary:
  print p.sentences[s]
