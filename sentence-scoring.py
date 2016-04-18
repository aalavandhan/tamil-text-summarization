#!/usr/bin/python
import sys
import operator
import math
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter

PATH        = sys.argv[1]
HEADING     = sys.argv[2]      if len(sys.argv) > 2 else ""
SIZE        = int(sys.argv[3]) if len(sys.argv) > 3 else 3

class SentenceScoreCalculator:
  def __init__(self, p):
    self.sCount = p.sCount
    self.pCount = p.pCount
    self.hWords = word_tokenize(HEADING.decode('UTF-8'))
    self.counter = WordCounter(p.sCount).count(p.processed)
    self.vocabulary = self.counter.wordDict.keys()
    self.paragraphStructure = p.paragraphStructure
    self.sentenceWords = p.processed

  def score(self, index):
    words = self.sentenceWords[index]
    return self.surfaceScore(index, words) + self.headingScore(index, words)

  def surfaceScore(self, index, words):
    return self.positionScore(index, words) + self.lengthScore(index, words) + self.paragraphScore(index, words)

  def paragraphScore(self, index, words):
    return 1 - ( self.paragraphStructure[index] / self.pCount )

  def headingScore(self, index, words):
    if len(self.hWords) == 0:
      return 0

    wordsInHeading = len(filter(lambda w: w in self.hWords, words))

    return float(wordsInHeading) / ( math.log( len(words) ) + math.log( len(self.hWords) ) )

  def positionScore(self, index, words):
    return 1 - ( index / self.sCount )

  def lengthScore(self, index, words):
    return len(words) / len(self.vocabulary)

p = Preprocessor(PATH, 1).parse()
scorer = SentenceScoreCalculator(p)

summary = sorted(sorted(range(p.sCount), key=lambda s: scorer.score(s), reverse=True)[0:SIZE])

for s in summary:
  print p.sentences[s]


