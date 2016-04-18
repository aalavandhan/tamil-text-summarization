import math
def euclideanDistance(vector1, vector2):
  dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
  dist = math.sqrt(sum(dist))
  return dist
