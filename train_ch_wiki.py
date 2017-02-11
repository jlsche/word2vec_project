import logging, sys, os.path
import multiprocessing

import jieba
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

useless_words = [' ', '\n', '\t']

class MySentences(object):
    def __init__(self, fname):
        self.fname = fname
        self.dirname = os.path.abspath(os.path.join((__file__), os.pardir))

    def __iter__(self):
        for line in open(self.dirname + "/data/" + self.fname):
            # if there is any further preprocess like encoding, lemma, ...
            # do it here, and then yield a list of utf8 words

            # zh_cn
            #simplified = opencc.convert(line, config='zhtw2zhcn_s.ini')
            #tokenized_line = jieba.lcut(simplified, cut_all=False)

            # zh_tw
            tokenized_line = jieba.lcut(line, cut_all=False)

            no_space = [x for x in tokenized_line if x not in useless_words]
            yield no_space

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) < 4:
        print(globals()['__doc__'])
        sys.exit(1)

    inp, outp_model, outp_vector = sys.argv[1:4]
    sentence_generator = MySentences(inp)

    model = Word2Vec(sentence_generator, size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(outp_model)
    model.save_word2vec_format(outp_vector, binary=False)
    logger.info("Finished Training Model")

