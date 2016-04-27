# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

STEMMER = "./util/tamil-stemmer/snowball/stemwords"

def stem(word):
  ST_Proc = Popen([STEMMER, "-l", "ta"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
  return ST_Proc.communicate(input=word.encode('UTF-8'))[0].strip('\n')
