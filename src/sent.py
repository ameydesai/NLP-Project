import traceback
import nltk.data
import nltk
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


def readInputFile():
    f = open("./input/00.16.28-8800.txt", "rb")
    data = f.read()
    return data
def readGoldFile():
    f = open("./gold/00.16.28-8800.gold", "rb")
    data = f.readlines()
    return data

        
def checkGrams(data, phrases):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    val = sent_detector.tokenize(data.strip())
    for sent in val:
        tokens = nltk.tokenize.word_tokenize(sent)
        tok_cnt = Counter(ngrams(tokens, 2))
        if p in sent:
            

def parsing(data, phrases):
    subjective = [] 
    objective = []
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    val = sent_detector.tokenize(data.strip())

    for sent in val:
        sub_tags = []
        obj_tags = []
        tok_sent = nltk.word_tokenize(sent)
        pos = nltk.pos_tag(tok_sent)
        sent_status = False
        for p in phrases:
            if p in sent:    
                for tags in pos:
                    sub_tags.append(tags[1])
                subjective.append(sub_tags)    
                #print p, "--",  sent, "--", pos
                sent_status = True
                break
        if not sent_status:
            for tags in pos:
                obj_tags.append(tags[1])
            objective.append(obj_tags)
    return subjective, objective

                #print pos
def main():
    input_data = readInputFile()
    gold_data = readGoldFile()
    
    phrases = getSubjPhrase(gold_data)
    checkGrams(input_data, phrases)
    #parsing(input_data, phrases)
if __name__ == '__main__':
    try:
        #nltk.download()
        main()
    except Exception as e:
        print traceback.print_exc()
