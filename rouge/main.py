import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize, sent_tokenize

from util.lcs import LCS
from util.wlcs import WLCS
from util.stemmer import stem

from math import sqrt

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def tokenize(text, grams=1):
  wordStems = lambda s: map(stem, word_tokenize(s))
  sentTokens = lambda tok, s: tok + wordStems(s)

  if grams == 1:
    return list(reduce(sentTokens, sent_tokenize(text), [ ]))
  else:
    return list(ngrams(reduce(sentTokens, sent_tokenize(text), [ ]), grams))

def rougeN(candidateSummary, refrenceSummaries, grams):
  candidateGrams = set(tokenize(candidateSummary, grams))
  refGrams = lambda s: set(tokenize(s, grams))
  rogueScore = lambda s: float(len(candidateGrams & refGrams(s))) / len(refGrams(s))

  return max(map(rogueScore, refrenceSummaries))

def rougeL(candidateSummary, refrenceSummaries):
  B = 1

  lcs  = lambda s: len( LCS(tokenize(candidateSummary), tokenize(s)) ) / 3
  Rlcs = lambda s: float(lcs(s)) / len(candidateSummary)
  Plcs = lambda s: float(lcs(s)) / len(s)

  Flcs = lambda s: (1 + B ** 2) * Rlcs(s) * Plcs(s) / ( Rlcs(s) + B ** 2 * Plcs(s) ) if lcs(s) > 0 else 0

  return max(map(Flcs, refrenceSummaries))

def rougeW(candidateSummary, refrenceSummaries):
  B = 1

  wlcs  = lambda s: WLCS(tokenize(candidateSummary), tokenize(s))
  Rlcs = lambda s: sqrt( float(wlcs(s)) / pow(len(candidateSummary),2) )
  Plcs = lambda s: sqrt( float(wlcs(s)) / pow(len(s),2) )

  Flcs = lambda s: (1 + B ** 2) * Rlcs(s) * Plcs(s) / ( Rlcs(s) + B ** 2 * Plcs(s) ) if wlcs(s) > 0 else 0

  return max(map(Flcs, refrenceSummaries))

def rougeS(candidateSummary, refrenceSummaries):
  B = 1

  candidateTokens = (tokenize(candidateSummary))
  refTokens = lambda s: (tokenize(s))
  skip2  = lambda s: len(skipgrams(candidateTokens,2,2) & skipgrams(refTokens(s),2,2))
  Rskip2 = lambda s: float(skip(s)) / nCr(len(candidateSummary),2)
  Pskip2 = lambda s: float(skip(s)) / nCr(len(s),2)

  Fskip2 = lambda s: (1 + B ** 2) * Rskip2(s) * Pskip2(s) / ( Rskip2(s) + B ** 2 * Pskip2(s) ) if skip2(s) > 0 else 0

  return max(map(Fskip2, refrenceSummaries))
