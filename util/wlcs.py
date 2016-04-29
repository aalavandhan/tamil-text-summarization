import math

def func(k):
	return pow(k,2)

def WLCS(wordsA, wordsB):
	cij = [[0 for j in range(len(wordsB)+1)] for i in range(len(wordsA)+1)]
	wij = [[0 for j in range(len(wordsB)+1)] for i in range(len(wordsA)+1

	for i, x in enumerate(wordsA):
    	for j, y in enumerate(wordsB):
      		if x == y:
      			k = wij[i-1][j-1]
      			cij[i][j] = cij[i-1,j-1] + func(k + 1) - func(k)
      			wij[i][j] = k + 1
      		  
      		else:
        		if c[i-1][j] > c[i][j-1]:
        			c[i][j] = c[i-1][j]
        			w[i][j] = 0
        		else:
        			c[i][j] = c[i][j-1]
        			w[i][j] = 0

    return cij[len(wordsA)][len(wordsB)]