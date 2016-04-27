import sys
import sklearn
import math

from util.preprocessor import Preprocessor
from util.word_counter import WordCounter
from sklearn.cluster   import KMeans
from util.distance     import euclideanDistance

def termWeightFN(s, counter, sCount, TYPE):
  sentencesWithWord = lambda w: filter(lambda sd: counter.isWordIn(sd, w), counter.sentenceDict)

  booL = lambda w: 1 if counter.isWordIn(s, w) else 0
  tF   = lambda w: counter.fetchSentenceWordCount(s, w) if counter.isWordIn(s, w) else 0
  idF  = lambda w: math.log( float(sCount) / len(sentencesWithWord(w)) ) if counter.isWordIn(s, w) else 0
  tFIdf= lambda w: tF(w) * idF(w)

  # BOOL
  if TYPE == 1:
    return (booL)

  # TF
  elif TYPE == 2:
    return (tF)

  # IDF
  elif TYPE == 3:
    return (idF)

  # TF-IDF
  elif TYPE == 4:
    return (tFIdf)

def normalizeFeatures(features):
  noramlized = [ ]
  for f in features:
    noramlized.append(map(lambda ft: float(ft) / max(f) if max(f) > 0 else 0, f))
  return noramlized


def buildFeatures(preprocessed, counter, TYPE):
  vocabulary = counter.vocabulary()

  features = [ ]

  for s in range(preprocessed.sCount):
    sFeatures = map(termWeightFN(s, counter, preprocessed.sCount, TYPE), vocabulary)
    features.append(sFeatures)

  return normalizeFeatures(features)

def sentenceSelect(kmeans, preprocessed, features):
  summary = [ ]

  for i in set(kmeans.labels_):
    sentencesInCluster = reduce(lambda m,l: m + [l] if kmeans.labels_[l] == i else m, range(preprocessed.sCount), [ ])

    sortedByClosenessToCentroid = sorted(sentencesInCluster, key=lambda s: euclideanDistance(kmeans.cluster_centers_[i], features[s]))

    summary.append(sortedByClosenessToCentroid[0])

  return summary


def generateSummary(PATH, NGRAMS, CLUSTERS, TYPE):
  # Preprocessing and Term Selection
  p = Preprocessor(PATH, NGRAMS).parse()
  counter = WordCounter(p.sCount).count(p.processed)

  # Term weighting and feature selection
  features = buildFeatures(p, counter, TYPE)

  # Sentence clustering
  kmeans = KMeans(n_clusters=CLUSTERS,
    #n_jobs=4,
    precompute_distances=True,
    init="k-means++",
    random_state=500,
    tol=1e-10,
    copy_x=True)
  kmeans.fit(features)

  #Sentence selection
  summary = sentenceSelect(kmeans, p, features)

  return map(lambda s: p.sentences[s], sorted(summary))

if __name__ == "__main__":
  PATH     = sys.argv[1]
  NGRAMS   = int(sys.argv[2]) if len(sys.argv) > 2 else 1
  CLUSTERS = int(sys.argv[3]) if len(sys.argv) > 3 else 3
  TYPE     = int(sys.argv[4]) if len(sys.argv) > 4 else 1

  # Print summary
  for s in generateSummary(PATH, NGRAMS, CLUSTERS, TYPE):
    print s
