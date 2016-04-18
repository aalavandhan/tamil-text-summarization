class WordCounter:
  def __init__(self, sCount):
    self.wordDict = { }
    self.sentenceDict = { }

    self.sCount = sCount

  def count(self, ngrams):
    for s in range(self.sCount):
      self.sentenceDict[s] = { }

      for w in ngrams[s]:
        word = w

        if word not in self.wordDict:
          self.wordDict[word] = 0

        if word not in self.sentenceDict[s]:
          self.sentenceDict[s][word] = 0

        self.wordDict[word] = self.wordDict[word] + 1
        self.sentenceDict[s][word] = self.sentenceDict[s][word] + 1

    return self
