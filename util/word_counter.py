from stemmer import stem
class WordCounter:
  def __init__(self, sCount):
    self.wordDict = { }
    self.sentenceDict = { }

    self.sCount = sCount

  def wordFromGram(self, gram):
    return gram

  def vocabulary(self):
    return self.wordDict.keys()

  def wordsIn(self, s):
    return self.fetchSentence(s)

  def fetchWordCount(self, gram):
    w = self.wordFromGram(gram)
    return self.wordDict[w] if w in self.wordDict else 0

  def fetchSentenceWordCount(self, s, gram):
    w = self.wordFromGram(gram)
    return self.sentenceDict[s][w] if w in self.sentenceDict[s] else 0

  def isWordIn(self, s, gram):
    w = self.wordFromGram(gram)
    return w in self.fetchSentence(s)

  def fetchSentence(self, s):
    return self.sentenceDict[s]

  def count(self, sentences):
    for s in range(self.sCount):
      self.sentenceDict[s] = { }

      for gram in sentences[s]:
        word = self.wordFromGram(gram)

        if word not in self.wordDict:
          self.wordDict[word] = 0

        if word not in self.sentenceDict[s]:
          self.sentenceDict[s][word] = 0

        self.wordDict[word] = self.wordDict[word] + 1
        self.sentenceDict[s][word] = self.sentenceDict[s][word] + 1

    return self
