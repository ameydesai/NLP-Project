from common import gold_dir, readOneGoldFile
import traceback
import glob
import nltk
import matplotlib.pyplot as plt
def readGoldFiles():
    counter = {}
    gold_fs = glob.glob(gold_dir)
    for fs in gold_fs:
        data = readOneGoldFile(fs)
        for op in data:
            words = op.strip().split("  ")[2]
            no_of_words = len(nltk.word_tokenize(words))
            if no_of_words in counter:
                counter[no_of_words] += 1
            else:
                counter[no_of_words] = 1
    return counter

            
def main():
    words_count  = readGoldFiles()
    x = words_count.keys()
    y = words_count.values()
    plt.xlabel("Words with size as x:")
    plt.ylabel("Number of words for x")
 
    #plt.plot(x, y)
    #plt.show()
    #plt.plot(x[:10], y[:10], 'ro')
    #plt.show()
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print traceback.print_exc()
