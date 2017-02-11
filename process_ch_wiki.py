import logging, os.path, sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) < 3:
        print(globals()['__doc__'])
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    i = 0

    with open(outp, 'w', encoding='utf-8') as handle:
        wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
        for text in wiki.get_texts():
            handle.write(b' '.join(text).decode('utf-8') + '\n')
            i += 1
            if (i % 10000) == 0:
                logger.info("Saved %d articles" % i)

    logger.info("Finished Saved %d articles" % i)

