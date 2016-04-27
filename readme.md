##Text Summarization in Tamil

###Method 1 - Sentence Scoring

[Refrence : Section 2.1](http://research.ijcaonline.org/volume75/number6/pxc3890449.pdf)

```bash
python sentence-scoring.py [ PATH TO FILE ] [ N-SUMMARY-SENTENCES ] [ FILE HEADING ]
# (eg) python sentence-clustering.py test/data/article-4 'மதுரை மீனாட்சி அம்மனுக்கு பட்டாபிஷேகம்' 3
```

###Method 2 - Sentence Weighing

[Refrence : Section 2.2](http://research.ijcaonline.org/volume75/number6/pxc3890449.pdf)

```bash
python sentence-weighing.py [ PATH TO FILE ]  [ N-SUMMARY-SENTENCES ]
# (eg) python sentence-clustering.py test/data/article-4 3
```

###Method 3 - Clustering Approach

[Refrence : Section 3.3](http://nlp.cic.ipn.mx/Publications/2008/Text%20Summarization%20by%20Sentence%20Extraction%20Using.pdf)

```bash
python sentence-clustering.py [ PATH TO FILE ] [ N-GRAMS ] [ N-CLUSTERS ] [ TERM-WEIGHT-TYPE ]
# TYPE = 1 -> Bool
# TYPE = 2 -> TF
# TYPE = 3 -> IDF
# TYPE = 4 -> TF-IDF
# (eg) python sentence-clustering.py test/data/article-4 3 3 4
```

----

Test data is present in `./test/data`

----
