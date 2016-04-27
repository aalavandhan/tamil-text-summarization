# https://github.com/Modelado/Longest-common-subsequence/blob/master/sub.py#L2

def LCS(wordsA, wordsB):
  longitud = [[0 for j in range(len(wordsB)+1)] for i in range(len(wordsA)+1)]

  for i, x in enumerate(wordsA):
    for j, y in enumerate(wordsB):
      if x == y:
        longitud[i+1][j+1] = longitud[i][j] + 1
      else:
        longitud[i+1][j+1] = max(longitud[i+1][j], longitud[i][j+1])

  resultado = ""
  x, y = len(wordsA), len(wordsB)
  while x != 0 and y != 0:
    if longitud[x][y] == longitud[x-1][y]:
      x -= 1
    elif longitud[x][y] == longitud[x][y-1]:
      y -= 1
    else:
      assert wordsA[x-1] == wordsB[y-1]
      resultado = wordsA[x-1] + resultado
      x -= 1
      y -= 1
  return resultado
