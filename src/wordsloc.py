from common import input_dir, gold_dir, readOneGoldFile, readOneInputFile, getSubjPhrase
import traceback
import glob
import nltk


def checkWordsLocation(id, gd, i, g):
    lt_mid = 0
    gt_mid = 0
    lt_mid2 = 0
    gt_mid2 = 0
    lt_mid3 = 0
    gt_mid3 = 0
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(id.strip())
    phrases = getSubjPhrase(gd)
    for sent in sentences:
        for p in phrases:
            if p in sent:
                tok_sent = nltk.word_tokenize(sent)
                tok_p = nltk.word_tokenize(p)
                if tok_p[0] not in tok_sent:
                    #print tok_p, tok_sent, i, g
                    continue
                ph_start_idx = tok_sent.index(tok_p[0]) 
                ph_end_idx = ph_start_idx + len(tok_p)
                ph_mid_idx = (ph_start_idx + ph_end_idx)/2
                sent_mid = len(tok_sent) / 2
                
                if ph_mid_idx < sent_mid:
                    lt_mid += 1
                    if ph_mid_idx < sent_mid/2:
                        lt_mid2 += 1
                    else:
                        gt_mid2 += 1
                else:
                    gt_mid +=1
                    if ph_mid_idx < sent_mid + sent_mid/2:
                        lt_mid3 += 1
                    else:
                        gt_mid3 += 1
                
    return (lt_mid, gt_mid, lt_mid2, gt_mid2, lt_mid3, gt_mid3, len(phrases))

def readFiles():
    input_fs = sorted(glob.glob(input_dir))
    gold_fs = sorted(glob.glob(gold_dir))
    overall_lt = 0
    overall_gt = 0
    overall_lt1 = 0
    overall_gt1 = 0
    overall_lt2 = 0
    overall_gt2 = 0

    overall_p = 0
    for (i, g) in zip(input_fs, gold_fs):
        input_data = readOneInputFile(i)
        gold_data = readOneGoldFile(g)
        stats = checkWordsLocation(input_data, gold_data, i, g)
        overall_lt += stats[0]
        overall_gt += stats[1]
        overall_lt1 += stats[2]
        overall_gt1 += stats[3]
        overall_lt2 += stats[4]
        overall_gt2 += stats[5]
 
        overall_p +=  stats[6] 
        
    print overall_lt, overall_gt, overall_lt1, overall_gt1, overall_lt2, overall_gt2, overall_p
def main():
    readFiles()
if __name__ == '__main__':
    try:
        #nltk.download()
        main()
    except Exception as e:
        print traceback.print_exc()
