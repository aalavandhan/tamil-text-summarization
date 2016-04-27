# -*- coding: utf-8 -*-
import os
import wikipedia
import re

from nltk.tokenize import sent_tokenize, word_tokenize

wikipedia.set_lang("ta")

TOPICS = [
  #"பல்லவர்",
  # Names of indian cities
  "சென்னை",
  "பெங்களூர்",
  "தில்லி",
  "கொல்கத்தா",
  "மும்பை"
]

SUMMARY_PATH = "../test/summaries"
ARTICLE_PATH = "../test/data"
TITLE_PATH   = "../test/title"

ELIMINATION_TRESHOLD = 0.1
PARAGRAPH_TRESHOLD = 15

SUMMARY_SIZE = 8


def getContentRichParagrahs(d):
  wordCount = { }
  paragraph = re.split("\n{1,}", d)

  for i in range(len(paragraph)):
    wordCount[i] = len( word_tokenize( paragraph[i] ) )

  maxwordCount = max(wordCount.values())

  # Filtering the very small lines
  selectedParagraphs = filter(lambda l: float(wordCount[l]) / maxwordCount >= ELIMINATION_TRESHOLD, wordCount.keys())

  return "\n".join( map(lambda l: paragraph[l], selectedParagraphs)[0:PARAGRAPH_TRESHOLD] )


def cleanContent(d, contentRich=False):
  d = re.sub(r'[a-zA-Z\(\)\'\"\[\]\*]', '', d)

  d = ( d if not contentRich else getContentRichParagrahs(d) )
  d = re.sub('\s{2,}', ' ', d)
  d = re.sub('\n{3,}', '\n\n', d)

  d = re.sub('[\.\s]?\.+', '.', d)
  d = re.sub('[\.\s]?\.+', '.', d)

  # HOT FIXES
  d = d.encode('UTF-8')
  d = re.sub('\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xaa\xe0\xae\xbf.', '\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xaa\xe0\xae\xbf', d)
  d = re.sub('\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xae\xe0\xaf\x80.', '\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xae\xe0\xaf\x80', d)
  d = re.sub('\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xae\xe0\xaf\x81.', '\xe0\xae\x95\xe0\xae\xbf.\xe0\xae\xae\xe0\xaf\x81', d)
  d = d.decode('UTF-8')

  return d

def cleanSummary(d):
  return "\n".join( sent_tokenize( cleanContent(d) )[0:SUMMARY_SIZE] )

def filterSummaryFromContent(content, summary):
  return content.replace(summary, '')


for i in range(len(TOPICS)):
  wiki = wikipedia.page(TOPICS[i])
  fileName = "article-" + str(i + 1)

  summary = wiki.summary
  content = filterSummaryFromContent(wiki.content, wiki.summary)
  title   = wiki.title

  open(os.path.join(SUMMARY_PATH, fileName), "w+").write(cleanSummary(summary).encode('UTF-8'))
  open(os.path.join(ARTICLE_PATH, fileName), "w+").write(cleanContent(content, contentRich=True).encode('UTF-8'))
  open(os.path.join(TITLE_PATH,   fileName), "w+").write(cleanContent(title).encode('UTF-8'))

  print TOPICS[i]
