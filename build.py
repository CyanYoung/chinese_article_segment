import json
import pickle as pk

import nltk

from gensim.models import Word2Vec


embed_len = 200
min_freq = 5

path_word_vec = 'feat/word_vec.pkl'


def word2vec(sents):
    sent_words = [sent.split() for sent in sents]
    model = Word2Vec(sent_words, size=embed_len, window=3, min_count=min_freq, negative=5, iter=10)
    word_vecs = model.wv
    with open(path_word_vec, 'wb') as f:
        pk.dump(model, f)
    if __name__ == '__main__':
        words = ['几', '元', '日']
        for word in words:
            print(word_vecs.most_similar(word))


def fit(path_train, path_cpd, train):
    with open(path_train, 'r') as f:
        sents = json.load(f)
    if train:
        word2vec(sents)
    all_words = ' '.join(sents).split()
    bgs = list(nltk.bigrams(all_words))
    cfd = nltk.ConditionalFreqDist(bgs)
    print()


if __name__ == '__main__':
    path_train = 'data/train.json'
    path_cpd = 'feat/cpd.pkl'
    fit(path_train, path_cpd, train=False)
