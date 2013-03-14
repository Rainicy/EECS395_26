# top level function
def nGramsFromString(message, n):
  return removeStopListNGrams(allNGramsFromString(message, n))



# old top level functions
def unigramsFromString(message):
  return removeStopListUnigrams(allUnigramsFromString(message))

def bigramsFromString(message):
  return removeStopListBigrams(allBigramsFromString(message))

# stop lists
from stopwords import stopwordslist
bad_characters = ',."`_-~!@#$%^&*()[]{}\\/;:><|+=?1234567890'


# privatish stuff
def unicodeStringToAscii(message):
    return message.encode('ascii', 'replace')

def removePunctuationFromString(message):
# TODO: more efficient version of this function
  m = message
  for c in bad_characters:
    m = m.replace(c, ' ')
  return m

def removeCharNumber(s, pos):
  return s[:pos]+s[pos+1:]

def removeExtraSpaces(s):
  s = s.strip()
  if len(s) < 1:
    return ''
  pos = 0
  while pos < len(s):
    if (s[pos]==' ') & (s[pos-1]==' '):
      s = removeCharNumber(s, pos)
    else:
      pos = pos + 1
  return s

def normalizeString(message):
  message = unicodeStringToAscii(message)
  message = removePunctuationFromString(message)
  message = message.lower()
  message = removeExtraSpaces(message)
  return message

# next steps:
#  - tokenize
#  -- bigrams and unigrams
#  -- remove stop words (from both)

def listContains(lst, it):
  return it in lst

# this is more efficient than set intersection
# or than flipping f and s
def listContainsAny(f,s):
  for t in s:
    if t in f:
      return True
  return False

def allUnigramsFromString(message):
  return message.split(' ')

# This function Author: Joel Nothman <jnothman@student.usyd.edu.au>
def nGramsIterator(sequence, n):
  sequence = iter(sequence)
  history = []
  while n > 1:
    history.append(sequence.next())
    n = n - 1
  for item in sequence:
    history.append(item)
    yield tuple(history)
    del history[0]

def bigramsIterator(sequence):
  return nGramsIterator(sequence, 2)

def allBigramsFromString(message):
  return allNGramsFromString(message,2)

def allNGramsFromString(message, n):
  message = allUnigramsFromString(message)
  grams = []
  for g in nGramsIterator(message,n):
    grams.append(g)
  return grams


def removeStopListNGrams(grams):
  x = lambda t: not(listContainsAny(stopwordslist, t))
  return filter(x, grams)

def removeStopListBigrams(bigrams):
  x = lambda b: not(
        listContains(stopwordslist, b[0]) | 
        listContains(stopwordslist, b[1]) )
  return filter(x, bigrams)

def removeStopListUnigrams(unigrams):
  x = lambda u: not(listContains(stopwordslist, u))
  return filter(x, unigrams)