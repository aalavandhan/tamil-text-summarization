import sys
import sklearn
import math

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter
from sklearn.cluster   import KMeans
from util.distance     import euclideanDistance

PATH     = sys.argv[1]
NGRAMS   = int(sys.argv[2]) if len(sys.argv) > 2 else 1
CLUSTERS = int(sys.argv[3]) if len(sys.argv) > 3 else 3
TYPE     = int(sys.argv[4]) if len(sys.argv) > 4 else 1


def termWeight(s, wordDict, sentenceDict, sCount):
  # BOOL
  if TYPE == 1:
    return (lambda w: 1 if w in sentenceDict[s] else 0)

  # TF
  elif TYPE == 2:
    return (lambda w: sentenceDict[s][w] if w in sentenceDict[s] else 0 )

  # IDF
  elif TYPE == 3:
    return (lambda w: math.log( sCount / len(filter(lambda sd: w in sd, sentenceDict.values())) ) if w in sentenceDict[s] else 0  )

  # TF-IDF
  elif TYPE == 4:
    return (lambda w: sentenceDict[s][w] * math.log( sCount / len(filter(lambda sd: w in sd, sentenceDict.values())) ) if w in sentenceDict[s] else 0  )

def normalizeFeatures(features):
  noramlized = [ ]
  for f in features:
    noramlized.append(map(lambda ft: float(ft) / max(f), f))
  return noramlized


def buildFeatures(preprocessed, counter):
  vocabulary = counter.wordDict.keys()

  features = [ ]

  for s in range(preprocessed.sCount):
    sFeatures = map(termWeight(s, counter.wordDict, counter.sentenceDict, preprocessed.sCount), vocabulary)
    features.append(sFeatures)

  return normalizeFeatures(features)

def sentenceSelect(kmeans, preprocessed, features):
  summary = [ ]

  for i in set(kmeans.labels_):
    sentencesInCluster = reduce(lambda m,l: m + [l] if kmeans.labels_[l] == i else m, range(preprocessed.sCount), [ ])

    sortedByClosenessToCentroid = sorted(sentencesInCluster, key=lambda s: euclideanDistance(kmeans.cluster_centers_[i], features[s]))

    summary.append(sortedByClosenessToCentroid[0])

  return summary


# Preprocessing and Term Selection
p = Preprocessor(PATH, NGRAMS).parse()
counter = WordCounter(p.sCount).count(p.processed)

# Term weighting and feature selection
features = buildFeatures(p, counter)

# Sentence clustering
kmeans = KMeans(n_clusters=CLUSTERS)
kmeans.fit(features)

#Sentence selection
summary = sentenceSelect(kmeans, p, features)

# Print summary
for s in sorted(summary):
  print p.sentences[s]

