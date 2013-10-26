import glob
import pickle
import nltk
'''
gold_fs = glob.glob("./gold/*.gold")
subjective_phrase = set()
for val in gold_fs:
    f = open(val, 'rb')
    data = f.readlines()
    for sent in data:
        phrase = sent.strip().split("  ")[2]
        words = phrase.split(" ")
        for word in words
        subjective_phrase.add(phrase)
    

'''
#f = open("subjective_phrase", "wb")
#pickle.dump(subjective_phrase, f)

f = open("subjective_phrase", "rb")
sp = pickle.load(f)
input_fs = glob.glob("./input/*.txt")
for val in input_fs:
    f = open(val, 'rb')
    data = f.read()
    text = nltk.word_tokenize(data)
    pos = nltk.pos_tag(text)
    for p in sp:
        if p  in data:
            
        
    break

