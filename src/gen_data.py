import traceback
import glob
from common import input_dir, gold_dir, readOneGoldFile, readOneInputFile, getSubjPhrase
import argparse
import random
def splitGen(no_fs, v):
    if v == 1:
        return 0, int(no_fs * 0.7)
    if v == 2:
        return int(no_fs * 0.3), no_fs

def writePhrase(op_f, gold_data):
    for val in gold_data:
        op_f.write(val)
        op_f.write("\n")

def readFiles(gen_v, op_fn):
    f1 = open("../data/" + op_fn + "input.train", "a")
    f2 = open("../data/" + op_fn + "gold.train", "a")
    f3 = open("../data/" + op_fn + "input.test", "a")
    f4 = open("../data/" + op_fn + "gold.test", "a")
    
    input_fs = sorted(glob.glob(input_dir))
    gold_fs = sorted(glob.glob(gold_dir))
    train_gold_fs = []
    train_input_fs = []
    test_input_fs = []
    test_gold_fs = []
    if gen_v == 4:
        for val in range(len(input_fs)):
            if random.random() > 0.5:
                train_gold_fs.append(gold_fs[val])
                train_input_fs.append(input_fs[val])
            else:
                test_gold_fs.append(gold_fs[val])
                test_input_fs.append(input_fs[val])
                
    else:
        if gen_v == 3:
            train_gold_fs = gold_fs[0 : int(len(input_fs) * 0.3)] + gold_fs[ int(len(input_fs) * 0.7) :]
            train_input_fs = input_fs[0 : int(len(input_fs) * 0.3)] + input_fs[ int(len(input_fs) * 0.7) :]
            test_gold_fs = gold_fs[int(len(input_fs) * 0.3) :int(len(input_fs) * 0.7) ]
            test_input_fs = input_fs[int(len(input_fs) * 0.3) : int(len(input_fs) * 0.7)]
        else:
            s, e = splitGen(len(input_fs), gen_v)
            
            train_gold_fs = gold_fs[s:e]
            train_input_fs = input_fs[s:e]
            if gen_v == 2:
                e = s
                s = 0
            else:
                s = e
                e = len(input_fs)
            print s, e
            test_gold_fs = gold_fs[s:e]
            test_input_fs = input_fs[s:e]

    for (i, g) in zip(train_input_fs, train_gold_fs):
        train_input_data = readOneInputFile(i)
        train_gold_data = getSubjPhrase(readOneGoldFile(g))
        f1.write(str(train_input_data))
        writePhrase(f2, train_gold_data)
        #f2.write(str(train_gold_data))
    for (i, g) in zip(test_input_fs, test_gold_fs):
        test_input_data = readOneInputFile(i)
        test_gold_data = getSubjPhrase(readOneGoldFile(g))
        f3.write(str(test_input_data))
        writePhrase(f4, test_gold_data)
        #f4.write(str(test_gold_data))
    f1.close()
    f2.close()
    f3.close()
    f4.close()
        
def main():
    parser = argparse.ArgumentParser(description = "Inputs for Training/Test generation")
    parser.add_argument('input', nargs = '+', help = "Enter 1 for 0-70, 2 for 30-100, 3 for 0-30,70-100, 4 for random")
    args = parser.parse_args()
    gen_v = int(args.input[0])
    op_fn = args.input[1]
    readFiles(gen_v, op_fn)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print traceback.print_exc()

