import sys
import operator
import math
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter

from util.distance     import editDistance

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
    words = self.counter.wordsIn(index)
    additionalOccurances = lambda w: ( self.counter.fetchWordCount(w) - self.counter.fetchSentenceWordCount(index, w) )

    return reduce(lambda s, w: additionalOccurances(w) / self.nWords, words, 0)

  def rank(self, index):
    return(self.sentenceWeight(index) + self.lsw[index])

def generateSummary(PATH, SIZE):
  p = Preprocessor(PATH, 1).parse()
  scorer = SentenceScoreCalculator(p)

  summary = sorted(
    sorted(
      range(p.sCount), key=lambda s: scorer.rank(s), reverse=True)[0:SIZE])

  return map(lambda s: p.sentences[s], summary)


if __name__ == "__main__":
  PATH        = sys.argv[1]
  SIZE        = int(sys.argv[2]) if len(sys.argv) > 2 else 3

  # Print summary
  for s in generateSummary(PATH, SIZE):
    print s
