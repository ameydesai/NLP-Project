from common import input_dir, gold_dir, readOneGoldFile, getSubjPhrase
import traceback
import glob
import nltk
import operator

def getPosCount():
    pos_counter = {}
    gold_fs = glob.glob(gold_dir)
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    for fs in gold_fs:
        data = readOneGoldFile(fs)
        for op in data:
            phrase = op.strip().split("  ")[2]
            words = nltk.tokenize.word_tokenize(phrase)
            pos = nltk.pos_tag(words)
            for p in pos:
                if p[1] in pos_counter:
                    pos_counter[p[1]] += 1
                else:
                    pos_counter[p[1]] = 1
    temp = sorted(pos_counter.items(), key = operator.itemgetter(1))
    for val in temp:
        print val
    #return pos_counter

def main():
     getPosCount()
if __name__ == '__main__':
    try:
        #nltk.download()
        main()
    except Exception as e:
        print traceback.print_exc()
