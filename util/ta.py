import re
# Accurately counting characters
# http://www.venkatarangan.com/blog/content/binary/Counting%20Letters%20in%20an%20Unicode%20String.pdf
def nChars(data):
  d = data if isinstance(data, unicode) else data.decode('UTF-8')

  TAMIL = u"[\u0B80-\u0BFF]"
  TAMILEXCLUSION = u"[\u25CC\u0B82\u0BBE-\u0BD7]"
  #KSHA  \u0B95\u0BCD\u0BB7 First three characters in KSHA sequence
  #SRI   \u0BB8\u0BCD\u0BB0\u0BC0
  TAMILKSHASRI = u"\u0B95\u0BCD\u0BB7|\u0BB8\u0BCD\u0BB0\u0BC0"
  matchedExclusion = re.findall(TAMILEXCLUSION, d)
  matchedKSHASRI   = re.findall(TAMILKSHASRI, d)
  matchedTamil     = re.findall(TAMIL, d)

  actualLength     = 0
  chkTamilLength   = 0
  excludedLength   = 0
  KSHASRILength    = 0

  if( matchedKSHASRI != None ):
    KSHASRILength = len(matchedKSHASRI)
  if( matchedExclusion != None ):
    excludedLength = len(matchedExclusion)
  if( matchedTamil != None ):
    chkTamilLength = len(matchedTamil)

  actualLength  = len(d) - KSHASRILength - excludedLength

  return(actualLength)
