#!/usr/bin/python
import sys
import operator
import math
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter

class SentenceScoreCalculator:
  def __init__(self, p, HEADING):
    self.sCount = p.sCount
    self.pCount = p.pCount
    self.hWords = word_tokenize(HEADING)
    self.counter = WordCounter(p.sCount).count(p.processed)
    self.vocabulary = self.counter.wordDict.keys()
    self.paragraphStructure = p.paragraphStructure
    self.sentenceWords = p.processed

  def score(self, index):
    words = self.sentenceWords[index]
    return self.surfaceScore(index, words) + self.headingScore(index, words)

  def surfaceScore(self, index, words):
    return (
      self.positionScore(index, words) +
      self.lengthScore(index, words) +
      self.paragraphScore(index, words)
    )

  def paragraphScore(self, index, words):
    return 1 - ( self.paragraphStructure[index] / self.pCount )

  def headingScore(self, index, words):
    if len(self.hWords) == 0:
      return 0

    wordsInHeading = len(filter(lambda w: w in self.hWords, words))
    totalWords = ( math.log( len(words) ) + math.log( len(self.hWords) ) )

    return float(wordsInHeading) / totalWords if totalWords > 0 else 0

  def positionScore(self, index, words):
    return 1 - ( index / self.sCount )

  def lengthScore(self, index, words):
    return len(words) / len(self.vocabulary)

def generateSummary(PATH, SIZE, HEADING):
  p = Preprocessor(PATH, 1).parse()
  scorer = SentenceScoreCalculator(p, HEADING)

  summary = sorted(
    sorted(
      range(p.sCount), key=lambda s: scorer.score(s), reverse=True)[0:SIZE])

  return map(lambda s: p.sentences[s], summary)


if __name__ == "__main__":
  PATH        = sys.argv[1]
  SIZE        = int(sys.argv[2]) if len(sys.argv) > 2 else 3
  HEADING     = sys.argv[3]      if len(sys.argv) > 3 else ""

  # Print summary
  for s in generateSummary(PATH, SIZE, HEADING):
    print s


