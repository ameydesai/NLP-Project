import nltk
import traceback
from common import input_dir, gold_dir, readOneGoldFile, readOneInputFile, getSubjPhrase
import glob
from nltk.corpus import stopwords


# Used when tokenizing words
sentence_re = r'''(?x)      # set flag to allow verbose regexps
      ([A-Z])(\.[A-Z])+\.?  # abbreviations, e.g. U.S.A.
    | \w+(-\w+)*            # words with optional internal hyphens
    | \$?\d+(\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
    | \.\.\.                # ellipsis
    | [][.,;"'?():-_`]      # these are separate tokens
'''


#Taken from Su Nam Kim Paper...
'''
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns
        
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
'''

grammar = r"""
 NBAR: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
      {<NNP>+}  
  NP:
    {<NBAR>}
    {<NBAR><IN><NBAR>}      # Chunk everything
    }<VBD|IN>+{      # Chink sequences of VBD and IN
  """

#grammar = ""
stopwords = stopwords.words('english')
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()



def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.node=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 100
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

def comparePhrase(t, g):
    phrases = getSubjPhrase(g)
    for term in t:
        for word in term:
            for p in phrases:
                if word in p:
                    print word, p
        print 
def printSubTrees(tree):
    for val in tree:
        print val
        print "--"

def conll_tag_chunks(chunk_sents):
    tag_sents = [nltk.chunk.tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in chunk_tags] for chunk_tags in tag_sents]


def keyPhrase(ip_data, gold_data):
    chunker = nltk.RegexpParser(grammar)
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(ip_data.strip())
    #sentences = "We saw the yellow dog"
    
    for sent in sentences:
        
        toks = nltk.regexp_tokenize(sent, sentence_re)
        postoks = nltk.tag.pos_tag(toks)
        tree = chunker.parse(postoks)
        print tree
        #print conll_tag_chunks(tree)
        #printSubTrees(tree)
        break
        #terms = get_terms(tree)
        #comparePhrase(terms, gold_data)

def readFiles():
    input_fs = sorted(glob.glob(input_dir))
    gold_fs = sorted(glob.glob(gold_dir))
    for (i, g) in zip(input_fs, gold_fs):
        input_data = readOneInputFile(i)
        gold_data = readOneGoldFile(g)
        keyPhrase(input_data, gold_data)
        break
def main():
    readFiles()
if __name__ == '__main__':
    try:
        #nltk.download()
        main()
    except Exception as e:
        print traceback.print_exc()
