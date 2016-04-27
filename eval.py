import sys
import os

from rouge.main import rougeN
from rouge.main import rougeL

from sentence_clustering import generateSummary as clusterSummary
from sentence_scoring    import generateSummary as scoreSummary
from sentence_weighing   import generateSummary as weightSummary

from util.freader import readAsString, readAsList

SPATH = "./test/summaries"
APATH = "./test/data"
TPATH = "./test/title"

def summaryString(s):
  return "\n".join( s )

for a in os.listdir(APATH)[0:1]:
  title = readAsString(os.path.join(TPATH, a))

  refSummaryList = readAsList(os.path.join(SPATH, a))
  refSummary = summaryString(refSummaryList)

  nSentences = len(refSummaryList)

  print refSummary
  print "---------------"

  # candidateSummary = summaryString( scoreSummary(os.path.join(APATH, a), nSentences, title) )
  # candidateSummary = summaryString( weightSummary(os.path.join(APATH, a), nSentences) )
  candidateSummary = summaryString( clusterSummary(os.path.join(APATH, a), 5, nSentences, 4) )

  print candidateSummary

  print rougeN(candidateSummary, [refSummary], 1)
  print rougeL(candidateSummary, [refSummary])

  print " "
