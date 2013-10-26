input_dir = "./input/*.txt"
gold_dir = "./gold/*.gold"
import glob
from itertools import tee, islice
from collections import Counter

def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break
def getSubjPhrase(data):
    phrases = set()
    for val in data:
        phrase = val.strip().split("  ")[2]
        phrases.add(phrase)
    return list(phrases)

def readOneInputFile(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    return data

def readOneGoldFile(fn):
    f = open(fn, 'rb')
    data = f.readlines()
    f.close()
    return data


