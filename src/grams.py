import traceback
import glob
import nltk
from itertools import tee, islice
from collections import Counter
from common import input_dir, gold_dir, ngrams, getSubjPhrase


def getBiGramsForSubjPhrase(data):
    bg_s = []
    for p in data:
        tok_p = nltk.tokenize.word_tokenize(p)
        if len(tok_p) == 1:
            bg_s.append((tok_p[0]))
        
        bg_p = Counter(ngrams(tok_p, 2))
        bg_k = bg_p.keys()
        for val in bg_k:
            bg_s.append(val)
    return bg_s

def getBiGrams(input_data, phrases, bg_subj_p):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(input_data.strip())
    for sent in sentences:
        words = nltk.tokenize.word_tokenize(sent)
        pos = nltk.pos_tag(words)
        #tok_cnt = Counter(ngrams(words, 2))
        pos_cnt = Counter(ngrams(pos, 2))
        #print tok_cnt, pos_cnt
        #break
        for p in phrases:
            if p in sent:
                bg_k = []
                tok_p = nltk.tokenize.word_tokenize(p)
                print tok_p
                '''
                if len(tok_p) == 1:
                    bg_k.append(tok_p[0])
                bg_p = Counter(ngrams(tok_p, 2))
                bg_k = bg_p.keys()
                print bg_k, tok_p
                '''
                break
def readFiles():
    input_fs = sorted(glob.glob(input_dir))
    gold_fs = sorted(glob.glob(gold_dir))
    for (i, g) in zip(input_fs, gold_fs):
        ip = open(i, 'rb')
        au = open(g, 'rb')
        ip_data = ip.read()
        gold_data = au.readlines()
        phrases = getSubjPhrase(gold_data)
        bg_subj_p = getBiGramsForSubjPhrase(phrases)
        getBiGrams(ip_data, phrases, bg_subj_p)
        break
def main():
    readFiles()
if __name__ == '__main__':
    try:
        #nltk.download()
        main()
    except Exception as e:
        print traceback.print_exc()
